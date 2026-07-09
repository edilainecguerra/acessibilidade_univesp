from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Polo, Indicador, Pergunta, Avaliacao, Resposta


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('selecionar_polo')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'checklist/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def selecionar_polo(request):
    polos = Polo.objects.filter(responsavel=request.user)
    if request.method == 'POST':
        polo_id = request.POST.get('polo_id')
        avaliacao = Avaliacao.objects.create(polo_id=polo_id)
        return redirect('questionario', avaliacao_id=avaliacao.id, indicador_numero=1)
    return render(request, 'checklist/selecionar_polo.html', {'polos': polos})


@login_required
def questionario(request, avaliacao_id, indicador_numero):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    indicador = get_object_or_404(Indicador, numero=indicador_numero)
    total_indicadores = Indicador.objects.count()
    perguntas = indicador.perguntas.all()

    if request.method == 'POST':
        for pergunta in perguntas:
            valor = request.POST.get(f'pergunta_{pergunta.id}')
            if valor:
                Resposta.objects.update_or_create(
                    avaliacao=avaliacao,
                    pergunta=pergunta,
                    defaults={'valor': valor}
                )
            elif pergunta.pergunta_mae:
                Resposta.objects.update_or_create(
                    avaliacao=avaliacao,
                    pergunta=pergunta,
                    defaults={'valor': 'nao'}
                )

        proximo = indicador_numero + 1
        if proximo <= total_indicadores:
            return redirect('questionario', avaliacao_id=avaliacao_id, indicador_numero=proximo)
        else:
            return redirect('resultado', avaliacao_id=avaliacao_id)

    # Monta numeração inteligente
    perguntas_numeradas = []
    contador_principal = 0
    contadores_sub = {}

    for pergunta in perguntas:
        if pergunta.pergunta_mae is None:
            contador_principal += 1
            contadores_sub[pergunta.pk] = 0
            tem_dependentes = pergunta.dependentes.exists()
            numero = str(contador_principal)
        else:
            mae_pk = pergunta.pergunta_mae.pk
            if mae_pk not in contadores_sub:
                contadores_sub[mae_pk] = 0
            contadores_sub[mae_pk] += 1
            mae_numero = next(
                (p['numero'] for p in perguntas_numeradas if p['pergunta'].pk == mae_pk), '?'
            )
            numero = f"{mae_numero}.{contadores_sub[mae_pk]}"
            tem_dependentes = False

        perguntas_numeradas.append({
            'pergunta': pergunta,
            'numero': numero,
            'tem_dependentes': tem_dependentes if pergunta.pergunta_mae is None else False,
        })

    return render(request, 'checklist/questionario.html', {
        'avaliacao': avaliacao,
        'indicador': indicador,
        'perguntas_numeradas': perguntas_numeradas,
        'indicador_numero': indicador_numero,
        'total_indicadores': total_indicadores,
    })


@login_required
def resultado(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    indicadores = Indicador.objects.all()
    resultado_por_indicador = []
    total_pontos = 0
    total_possiveis = 0

    for indicador in indicadores:
        perguntas = indicador.perguntas.all()
        respostas = Resposta.objects.filter(avaliacao=avaliacao, pergunta__in=perguntas)

        pontos = 0
        possiveis = 0
        for resposta in respostas:
            possiveis += resposta.pergunta.peso
            if resposta.valor == 'sim':
                pontos += resposta.pergunta.peso

        score = round((pontos / possiveis) * 100) if possiveis > 0 else 0
        total_pontos += pontos
        total_possiveis += possiveis

        resultado_por_indicador.append({
            'indicador': indicador,
            'score': score,
            'pontos': round(pontos, 1),
            'possiveis': round(possiveis, 1),
        })

    score_geral = round((total_pontos / total_possiveis) * 100) if total_possiveis > 0 else 0

    if score_geral >= 90:
        classificacao = ('Excelente', 'success')
    elif score_geral >= 70:
        classificacao = ('Bom', 'primary')
    elif score_geral >= 50:
        classificacao = ('Regular', 'warning')
    elif score_geral >= 30:
        classificacao = ('Crítico', 'danger')
    else:
        classificacao = ('Inadequado', 'dark')

    avaliacao.score_total = score_geral
    avaliacao.status = 'concluida'
    avaliacao.save()

    return render(request, 'checklist/resultado.html', {
        'avaliacao': avaliacao,
        'resultado_por_indicador': resultado_por_indicador,
        'score_geral': score_geral,
        'classificacao': classificacao,
    })

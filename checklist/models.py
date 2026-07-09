from django.db import models
from django.contrib.auth.models import User


class Polo(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.cidade}"


class Indicador(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=200)
    condicional = models.BooleanField(default=False)

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return f"{self.numero}. {self.nome}"


class Pergunta(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.TextField()
    referencia_nbr = models.CharField(max_length=100, blank=True)
    peso = models.FloatField(default=1.0)
    pergunta_mae = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='dependentes'
    )
    ordem = models.IntegerField()

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return f"{self.indicador.numero}.{self.ordem} - {self.texto[:60]}"


class Avaliacao(models.Model):
    STATUS = [('rascunho', 'Rascunho'), ('concluida', 'Concluída')]
    polo = models.ForeignKey(Polo, on_delete=models.CASCADE, related_name='avaliacoes')
    data = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default='rascunho')
    score_total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Avaliação {self.polo.nome} - {self.data}"


class Resposta(models.Model):
    OPCOES = [('sim', 'Sim'), ('nao', 'Não')]
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='respostas')
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    valor = models.CharField(max_length=3, choices=OPCOES)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pergunta} → {self.valor}"

# ♿ Sistema de Avaliação de Acessibilidade dos Polos UNIVESP

> Aplicação web desenvolvida no âmbito do Programa de Iniciação Científica e Tecnológica Voluntária (PICTV) da Universidade Virtual do Estado de São Paulo (UNIVESP), com o objetivo de avaliar as condições de acessibilidade arquitetônica dos polos presenciais do Estado de São Paulo.

---

## 📋 Sobre o Projeto

Este sistema permite que os responsáveis pelos polos presenciais da UNIVESP respondam a um **checklist digital de acessibilidade**, baseado na **NBR 9050/2004** e no **Manual de Acessibilidade Espacial para Escolas (MEC/UFSC, 2009)**, adaptado para o contexto da educação superior.

A ferramenta foi desenvolvida como protótipo funcional para demonstrar a viabilidade de um sistema de monitoramento contínuo da acessibilidade nos polos UNIVESP.

---

## 🏗️ Estrutura da Avaliação

O questionário é organizado em **10 indicadores**, adaptados dos 17 ambientes originais do manual:

| # | Indicador |
|---|-----------|
| 1 | Rua em frente ao polo |
| 2 | Portão até porta de entrada |
| 3 | Recepção e salas de atendimento |
| 4 | Corredores |
| 5 | Escadas |
| 6 | Rampas |
| 7 | Salas de aula |
| 8 | Sanitários |
| 9 | Trocador / Apoio à maternidade |
| 10 | Refeitório (condicional) |

---

## 🌡️ Sistema de Pontuação

As respostas são ponderadas por tipo de pergunta:

- **Perguntas principais** (existência do elemento): peso **1,0**
- **Perguntas complementares** (qualidade do elemento): peso **0,5**
- Perguntas complementares só aparecem quando a pergunta principal é respondida com **Sim**

| Faixa | Classificação |
|-------|--------------|
| 90–100% | ✅ Excelente |
| 70–89% | 🟢 Bom |
| 50–69% | 🟡 Regular |
| 30–49% | 🟠 Crítico |
| 0–29% | 🔴 Inadequado |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.14**
- **Django 6.0**
- **SQLite** (desenvolvimento)
- **Bootstrap 5**
- **JavaScript** (interatividade do questionário)
- **HTML5 / CSS3**

---

## 🚀 Como Instalar e Rodar

### Pré-requisitos
- Python 3.10+
- Git

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/edilainecguerra/acessibilidade_univesp.git
cd acessibilidade_univesp

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Instale as dependências
pip install django

# 4. Rode as migrações
python manage.py migrate

# 5. Carregue as perguntas do questionário
python manage.py loaddata fixture_checklist.json

# 6. Crie um superusuário
python manage.py createsuperuser

# 7. Inicie o servidor
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## ⚙️ Funcionalidades

- 🔐 **Autenticação** — login por responsável de polo
- 🏫 **Seleção de polo** — cada usuário acessa seu polo
- 📋 **Questionário adaptativo** — perguntas complementares aparecem condicionalmente
- 🔔 **Pop-up de transição** — alerta ao iniciar cada novo indicador
- 🌡️ **Resultado classificatório** — score geral e por indicador
- 📊 **Painel administrativo** — gestão completa via Django Admin
- 📁 **Histórico de avaliações** — registro de todas as avaliações realizadas

---

## 📚 Referências

- ABNT. **NBR 9050**: Acessibilidade a edificações, mobiliário, espaços e equipamentos urbanos. Rio de Janeiro, 2004.
- BRASIL. Ministério da Educação. **Manual de Acessibilidade Espacial para Escolas: o direito à escola acessível**. MEC/SEESP, 2009.
- BRASIL. **Constituição da República Federativa do Brasil de 1988**.
- BRASIL. **Lei nº 10.098**, de 19 de dezembro de 2000.
- LOUZADA, J. C. A.; MARTINS, S. E. S. O. (org.). **Inclusão e acessibilidade no ensino superior: das políticas às práticas inclusivas**. São Paulo: Cultura Acadêmica, 2025.

---

## 👩‍💻 Autora

Desenvolvido por **Edilaine C. Guerra**
Programa de Iniciação Científica e Tecnológica Voluntária — PICTV
Universidade Virtual do Estado de São Paulo — UNIVESP

---

> *"A acessibilidade destinada às pessoas com deficiência não constitui mera faculdade administrativa, mas uma exigência diretamente vinculada ao texto constitucional."*

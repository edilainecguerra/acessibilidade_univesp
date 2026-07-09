import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acessibilidade_univesp.settings')
django.setup()

from checklist.models import Pergunta

# ─── 1. Corrigir textos ───────────────────────────────────────────────
Pergunta.objects.filter(pk=40).update(
    texto="O mobiliário existente na recepção está posicionado de forma a não obstruir a circulação de pessoas?"
)
Pergunta.objects.filter(pk=53).update(
    texto="Os corredores estão livres de obstáculos como lixeiras, bebedouros, extintores, vasos de plantas, móveis e placas que atrapalhem a passagem?"
)
Pergunta.objects.filter(pk=99).update(
    texto="A rampa tem tamanho, inclinação e formato de acordo com a NBR 9050/04 seção 6.5 (inclinação máxima de 8,33%, comprimento máximo de 9m por segmento e largura mínima de 1,20m)?"
)

# ─── 2. Excluir perguntas do trocador (139–151) ───────────────────────
Pergunta.objects.filter(pk__in=[139, 140, 141, 142, 151]).delete()

# ─── 3. Definir pesos e dependências ─────────────────────────────────
# Formato: pk -> (peso, pk_mae)
atualizacoes = {
    # Indicador 1
    1:  (1.0, None),
    2:  (1.0, None),
    3:  (1.0, None),
    4:  (1.0, None),
    5:  (1.0, None),
    6:  (0.5, 5),
    7:  (0.5, 5),
    8:  (0.5, 5),
    9:  (0.5, 5),
    10: (1.0, None),
    11: (0.5, 10),
    12: (0.5, 10),
    13: (1.0, None),
    14: (0.5, 13),
    15: (0.5, 13),
    16: (0.5, 13),
    17: (0.5, 13),
    18: (0.5, 13),
    19: (0.5, 13),
    20: (0.5, 13),
    # Indicador 2
    21: (1.0, None),
    22: (1.0, None),
    23: (1.0, None),
    24: (0.5, 23),
    25: (0.5, 23),
    26: (0.5, 23),
    27: (0.5, 23),
    28: (0.5, 23),
    29: (0.5, 23),
    30: (1.0, None),
    31: (1.0, None),
    32: (1.0, None),
    33: (0.5, 32),
    34: (0.5, 32),
    35: (0.5, 32),
    36: (0.5, 32),
    37: (0.5, 32),
    # Indicador 3
    38: (1.0, None),
    39: (1.0, None),
    40: (1.0, None),
    41: (1.0, None),
    42: (1.0, None),
    43: (1.0, None),
    44: (1.0, None),
    45: (1.0, None),
    46: (1.0, None),
    47: (0.5, 46),
    48: (1.0, None),
    49: (1.0, None),
    50: (0.5, 49),
    51: (0.5, 49),
    # Indicador 4
    52: (1.0, None),
    53: (1.0, None),
    54: (0.5, 53),
    55: (1.0, None),
    56: (1.0, None),
    57: (1.0, None),
    58: (1.0, None),
    59: (1.0, None),
    60: (1.0, None),
    61: (0.5, 60),
    62: (1.0, None),
    63: (1.0, None),
    64: (1.0, None),
    65: (1.0, None),
    66: (1.0, None),
    67: (1.0, None),
    68: (0.5, 67),
    69: (1.0, None),
    70: (1.0, None),
    71: (0.5, 70),
    72: (0.5, 70),
    73: (0.5, 70),
    74: (1.0, None),
    75: (0.5, 74),
    76: (1.0, None),
    # Indicador 5
    77: (1.0, None),
    78: (1.0, None),
    79: (1.0, None),
    80: (1.0, None),
    81: (1.0, None),
    82: (1.0, None),
    83: (1.0, None),
    84: (1.0, None),
    85: (0.5, 84),
    86: (1.0, None),
    87: (1.0, None),
    88: (1.0, None),
    89: (0.5, 88),
    90: (0.5, 88),
    91: (0.5, 88),
    92: (0.5, 88),
    # Indicador 6
    93: (1.0, None),
    94: (0.5, 93),
    95: (0.5, 93),
    96: (0.5, 93),
    97: (0.5, 93),
    98: (0.5, 93),
    99: (0.5, 93),
    100: (0.5, 93),
    101: (0.5, 93),
    102: (0.5, 93),
    103: (0.5, 93),
    104: (0.5, 93),
    105: (0.5, 93),
    106: (0.5, 93),
    # Indicador 7
    107: (1.0, None),
    108: (1.0, None),
    109: (1.0, None),
    110: (1.0, None),
    111: (1.0, None),
    112: (0.5, 111),
    113: (0.5, 111),
    # Indicador 8
    114: (1.0, None),
    115: (0.5, 114),
    116: (0.5, 114),
    117: (0.5, 114),
    118: (0.5, 114),
    119: (0.5, 114),
    120: (0.5, 114),
    121: (0.5, 114),
    122: (0.5, 114),
    123: (0.5, 114),
    124: (0.5, 114),
    125: (0.5, 114),
    126: (0.5, 114),
    127: (0.5, 114),
    128: (0.5, 114),
    129: (0.5, 114),
    130: (0.5, 114),
    131: (0.5, 114),
    132: (0.5, 114),
    # Indicador 9
    133: (1.0, None),
    134: (0.5, 133),
    135: (0.5, 133),
    136: (0.5, 133),
    137: (0.5, 133),
    138: (0.5, 133),
    # Indicador 10
    143: (1.0, None),
    144: (0.5, 143),
    145: (0.5, 143),
    146: (0.5, 143),
    147: (0.5, 143),
    148: (0.5, 143),
    149: (0.5, 143),
    150: (0.5, 143),
}

atualizados = 0
for pk, (peso, mae_pk) in atualizacoes.items():
    try:
        p = Pergunta.objects.get(pk=pk)
        p.peso = peso
        p.pergunta_mae = Pergunta.objects.get(pk=mae_pk) if mae_pk else None
        p.save()
        atualizados += 1
    except Pergunta.DoesNotExist:
        print(f"⚠️  PK {pk} não encontrada, pulando...")

print(f"✅ {atualizados} perguntas atualizadas com sucesso!")
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acessibilidade_univesp.settings')
django.setup()

from django.contrib.auth.models import User
from checklist.models import Polo

# Busca o usuário univesp
usuario = User.objects.get(username='univesp')

# Remove polos existentes (exceto o fictício)
Polo.objects.exclude(nome='Polo Fictício - UNIVESP').delete()

# Cadastra os 402 polos
polos = []
for i in range(1, 403):
    polos.append(Polo(
        nome=f'Polo {i}',
        cidade=f'Polo {i}',
        responsavel=usuario
    ))

Polo.objects.bulk_create(polos)
print(f'✅ {Polo.objects.count()} polos cadastrados com sucesso!')
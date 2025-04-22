import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tatu_backend.settings')
django.setup()

from core.models import Kafedra

# List of names
names = [
    "Axborot texnologiyalari",
    "Dasturiy injiniring",
    "Kompyuter tizimlari",
    "Tabiiy fanlar",
    "Axborot ta’lim texnologiyalari",
    "Telekommunikatsiya injiniring",
    "Gumanitar va ijtimoiy fanlar",
    "Tillar kafedrasi",
    "Axborot xavfsizligi"
]

for name in names:
    Kafedra.objects.create(name=name)

from django.contrib import admin
from .models import Navigators, Mentorados, DisponibilidadeDeHorarios, Reuniao

# Register your models here.
admin.site.register(Navigators)
admin.site.register(Mentorados)
admin.site.register(DisponibilidadeDeHorarios)
admin.site.register(Reuniao)
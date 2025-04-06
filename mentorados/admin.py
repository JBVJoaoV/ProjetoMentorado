from django.contrib import admin
from .models import Navigators, Mentorados, DisponibilidadeDeHorarios

# Register your models here.
admin.site.register(Navigators)
admin.site.register(Mentorados)
admin.site.register(DisponibilidadeDeHorarios)
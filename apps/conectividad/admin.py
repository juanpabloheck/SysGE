from django.contrib import admin
from .models import Conectividad
from .forms import ConectividadForm


class ConectividadAdmin(admin.ModelAdmin):
    form = ConectividadForm
    list_display = ('sede', 'fecha_de_registro', 'hay_conectividad', 'velocidad_de_subida', 'velocidad_de_bajada')
    list_filter = ('sede',)


admin.site.register(Conectividad, ConectividadAdmin)

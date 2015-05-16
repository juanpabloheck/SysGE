from django.contrib import admin
from .models import MotivoInasistencia, TipoClase

class MotivoInasistenciaAdmin(admin.ModelAdmin):
    model = MotivoInasistencia

class TipoClaseAdmin(admin.ModelAdmin):
    model = TipoClase

admin.site.register(MotivoInasistencia, MotivoInasistenciaAdmin)
admin.site.register(TipoClase, TipoClaseAdmin)
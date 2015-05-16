from django.contrib import admin
from .forms import AsistenciaFormAdmin, AsistenciaMasivaFromAdmin
from .models import Asistencia, AsistenciaMasiva, MotivoInasistencia
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin.helpers import ActionForm
import datetime

# ************************* ASISTENCIA *******************************
class AsistenciaActionForm(ActionForm):
    fecha = forms.DateField(widget=AdminDateWidget())
    motivo = forms.ModelChoiceField(queryset=MotivoInasistencia.objects.all())


def poner_presente(modeladmin, request, queryset):
    fecha = request.POST['fecha']
    fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").strftime("%Y-%m-%d")
    motivo = MotivoInasistencia(request.POST['motivo'])
    cont = 0
    for alu in queryset:
        obj = Asistencia.objects.create(alumno=alu, fecha=fecha, presente="P", motivo=motivo)
        Asistencia.save(obj)
        cont += 1
    if alu:
        modeladmin.message_user(request, "%s actualizo correctamente." % "%s Asistencia se" % cont)
    else:
        modeladmin.message_user(request, "%s No se actualizo ninguna Asistencia.")
    poner_presente.short_description = "Poner presente"


def poner_ausente(modeladmin, request, queryset):
    fecha = request.POST['fecha']
    fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").strftime("%Y-%m-%d")
    motivo = MotivoInasistencia(request.POST['motivo'])
    cont = 0
    if motivo is None:
        modeladmin.message_user(request, "Debe seleccionar un Motivo de Inasistencia.")
    else:
        for alu in queryset:
            obj = Asistencia.objects.create(alumno=alu, fecha=fecha, presente="A", motivo=motivo)
            Asistencia.save(obj)
            cont += 1
            if alu:
                modeladmin.message_user(request, "%s actualizo correctamente." % "%s Inasistencia se" % cont)
            else:
                modeladmin.message_user(request, "%s No se actualizo ninguna Inasistencia.")
    poner_ausente.short_description = "Poner Ausente"


class AsistenciaAdmin(admin.ModelAdmin):
    form = AsistenciaFormAdmin
    raw_id_fields = ("alumno",)
    list_display = ('alumno', 'fecha', 'presente', 'motivo')
    search_fields = ('alumno__apellido', 'alumno__nombre',)
    list_filter = ('alumno', 'alumno__sede',)

# ************************* ASISTENCIA MASIVA*******************************

class AsistenciaMasivaAdmin(admin.ModelAdmin):
    form = AsistenciaMasivaFromAdmin
    action_form = AsistenciaActionForm
    actions = (poner_presente, poner_ausente)
    list_display = ('nombre', 'apellido', 'dni')
    #list_display = ('alumnos',)
    list_filter = ('sede',)

    def has_add_permission(self, request):
        return False


admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(AsistenciaMasiva, AsistenciaMasivaAdmin)
from django.contrib import admin
from .forms import IntervencionFormAdmin, TrabajosAprobadosFormAdmin
from .models import Intervencion, TrabajosAprobados

#***********************INTERVENCIONES*************************
class IntervencionAdmin(admin.ModelAdmin):
    form = IntervencionFormAdmin
    exclude = ('usuario',)
    raw_id_fields = ("alumno",)
    list_display = ('alumno', 'profesor', 'clase', 'observaciones', 'creado', 'modificado',)
    search_fields = ('alumno__apellido', 'alumno__nombre', 'profesor__nombre', 'profesor__apellido', 'clase__nombre_de_clase',)
    list_filter = ('alumno', 'profesor')


    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def queryset(self, request):
        qs = super(IntervencionAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(usuario=request.user)

#***********************TRABAJOS APROBADOS*************************
class TrabajosAprobadosAdmin(admin.ModelAdmin):
    form = TrabajosAprobadosFormAdmin
    exclude = ('usuario',)
    raw_id_fields = ("alumno",)
    list_display = ('alumno', 'profesor', 'clase', 'fecha_de_entrega','nota_simbolica', 'observaciones', 'creado', 'modificado')
    search_fields = ('alumno__apellido', 'alumno__nombre', 'profesor__apellido', 'profesor__nombre', 'clase__nombre_de_clase')
    list_filter = ('alumno', 'profesor')

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def queryset(self, request):
        qs = super(TrabajosAprobadosAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(usuario=request.user)

#*********************** PUBLICAR EN EL ADMIN
admin.site.register(Intervencion, IntervencionAdmin)
admin.site.register(TrabajosAprobados, TrabajosAprobadosAdmin)

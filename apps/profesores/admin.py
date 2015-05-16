# -*- coding: utf-8 -*-
from django.contrib import admin
from .forms import MateriaAdminForm, ProfesorAdminForm, ClaseAdminForm
from .models import Materia, Profesor, Clase
from django.contrib.auth.models import User

#********************* MATERIA********************************
class MateriaAdmin(admin.ModelAdmin):
    form = MateriaAdminForm
    list_display = ('nombre',)
    search_fields = ('nombre',)

#********************* CLASE ********************************
class ClaseInline(admin.TabularInline):
    model = Clase
    extra = 1

class ClaseAdmin(admin.ModelAdmin):
    form = ClaseAdminForm
    exclude = ('usuario',)
    #list_select_related = ('usuario',)
    list_display = ('nombre_de_clase', 'profesor',)
    search_fields = ('nombre_de_clase',)
    list_filter = ('profesor',)

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def queryset(self, request):
        qs = super(ClaseAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(usuario=request.user)

#********************* PROFESOR********************************
class ProfesorAdmin(admin.ModelAdmin):
    form = ProfesorAdminForm
    list_display = ('nombre_completo', 'dni', 'cuil', 'get_materias', 'get_tutor_de_sedes')
    search_fields = ('nombre', 'apellido', 'dni', 'cuil')
    inlines = [ClaseInline,]


    suit_form_tabs = (('info_personal', 'Información Personal'), ('info_academica', 'Información Academica'),)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info_personal',),
            'fields': ['nombre', 'apellido', 'dni', 'cuil', 'direccion', 'localidad', 'telefono_fijo', 'telefono_cel', 'email',]
        }),
        ('Información Adicional', {
            'classes': ('suit-tab', 'suit-tab-info_academica',),
            'fields': ['materias', 'tutor_de_sede', 'dedicacion_horaria', 'titulo', 'formacion_en_tics',]
        }),
    ]

#********************** PUBLICAR EN EL ADMIN***************************
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Clase, ClaseAdmin)
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Sede, Alumno, Coordinador
from .forms import SedeAdminForm, AlumnoAdminForm, CoordinadorAdminForm

#******************************SEDE**********************************
class SedeAdmin(admin.ModelAdmin):
    form = SedeAdminForm
    #inlines = [AlumnoInLine]
    list_display = ('nombre', 'cue', 'latitud', 'longitud')
    search_fields = ('nombre', 'cue')

#*************************** ALUMNO ********************************
def pasar_a_segundo_ano(modeladmin, request, queryset):
    queryset.update(ano_de_cursado='2')
    pasar_a_segundo_ano.short_description = "Pasar a segundo año"

def pasar_a_tercer_ano(modeladmin, request, queryset):
    queryset.update(ano_de_cursado='3')
    pasar_a_tercer_ano.short_description = "Pasar a tercer año"

def pasar_a_cuarto_ano(modeladmin, request, queryset):
    queryset.update(ano_de_cursado='4')
    pasar_a_cuarto_ano.short_description = "Pasar a cuarto año"

def pasar_a_quinto_ano(modeladmin, request, queryset):
    queryset.update(ano_de_cursado='5')
    pasar_a_quinto_ano.short_description = "Pasar a quinto año"

class AlumnoAdmin(admin.ModelAdmin):
    form = AlumnoAdminForm
    list_display = ('nombre_completo', 'dni', 'cuil', 'edad', 'estado', 'ano_de_cursado')
    search_fields = ('nombre', 'apellido', 'dni', 'cuil')
    list_filter = ('sede__nombre', 'genero', 'estado', 'pueblos_originarios', 'anio_de_ingreso')
    actions = (pasar_a_segundo_ano, pasar_a_tercer_ano, pasar_a_cuarto_ano, pasar_a_quinto_ano,)

    suit_form_tabs = (('info_personal', 'Información Personal'), ('info_adicional', 'Información Adicional'), ('info_tutor', 'Información del Tutor'))
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info_personal',),
            'fields': ['nombre', 'apellido', 'dni', 'cuil', 'sede', 'genero', 'fecha_de_nacimiento', 'edad', 'activo', 'estado', 'ano_de_cursado']
        }),
        ('Información Adicional', {
            'classes': ('suit-tab', 'suit-tab-info_adicional',),
            'fields': ['situacion', 'discapacidad', 'pueblos_originarios', 'anio_de_ingreso', 'asignacion_universal',]
        }),
        ('Información del Tutor', {
            'classes': ('suit-tab', 'suit-tab-info_tutor',),
            'fields': ['dni_tutor', 'nombre_tutor', 'apellido_tutor', 'cuil_tutor', 'parentesco',]
        })
    ]

# ********************** COORDINADOR **********************************
class CoordinadorAdmin(admin.ModelAdmin):
    form = CoordinadorAdminForm
    list_display = ('nombre_completo', 'dni', 'cuil')
    search_fields = ('nombre', 'apellido', 'dni', 'cuil')
    list_filter = ('sede__nombre',)

    suit_form_tabs = (('info_personal', 'Información Personal'), ('info_academica', 'Información Academica'),)
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-info_personal',),
            'fields': ['nombre', 'apellido', 'dni', 'cuil', 'sede', 'direccion', 'localidad', 'telefono_fijo', 'telefono_cel', 'email',]
        }),
        ('Información Adicional', {
            'classes': ('suit-tab', 'suit-tab-info_academica',),
            'fields': ['dedicacion_horaria', 'titulo', 'formacion_en_tics',]
        }),
    ]

admin.site.register(Sede, SedeAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Coordinador, CoordinadorAdmin)


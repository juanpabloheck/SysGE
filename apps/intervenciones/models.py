# -*- coding: utf-8 -*-
from django.db import models
from apps.sedes.models import Alumno
from apps.profesores.models import Profesor, Clase
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

#**************************INTERVENCIONES********************************
class Intervencion(models.Model):
    alumno = models.ForeignKey(Alumno)
    profesor = models.ForeignKey(Profesor)
    clase = ChainedForeignKey(
        Clase,
        chained_field="profesor",
        chained_model_field="profesor",
        show_all=False,
        auto_choose=True
    )
    observaciones = models.TextField(max_length=250, blank=True, null=True)
    creado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.alumno.nombre_completo()

#**************************TRABAJO APROBADOS********************************
class TrabajosAprobados(models.Model):
    alumno = models.ForeignKey(Alumno)
    profesor = models.ForeignKey(Profesor)
    clase = ChainedForeignKey(
        Clase,
        chained_field="profesor",
        chained_model_field="profesor",
        show_all=False,
        auto_choose=True
    )
    fecha_de_entrega = models.DateField()
    nota_simbolica = models.IntegerField(max_length=2)
    observaciones = models.TextField(max_length=200, blank=True, null=True)
    creado = models.DateField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.alumno.nombre_completo()

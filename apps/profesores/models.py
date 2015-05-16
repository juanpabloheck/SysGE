# -*- coding: utf-8 -*-
from django.db import models
from apps.sedes.models import Sede
from apps.configuraciones.models import TipoClase
from django.contrib.auth.models import User

#********************* VAARIABLES*************************
tipo_sino = (
    ('no', 'NO'),
    ('si', 'SI'),
)

#***************************** MODELO MATERIA**********************************
class Materia(models.Model):
      nombre = models.CharField(max_length=150)
      plan_de_estudio = models.TextField(max_length=200)

      def __unicode__(self):
         return self.nombre

#***************************** MODELO PROFESOR **********************************
class Profesor(models.Model):
      nombre = models.CharField(max_length=100)
      apellido = models.CharField(max_length=50)
      dni = models.IntegerField(max_length=8, verbose_name='DNI')
      cuil = models.CharField(max_length=13, verbose_name='CUIL')
      tutor_de_sede = models.ManyToManyField(Sede, related_name='Tutor de Sede')
      direccion = models.CharField(max_length=100, blank=True, null=True)
      localidad = models.CharField(max_length=100, blank=True, null=True)
      telefono_fijo = models.IntegerField(blank=True, null=True)
      telefono_cel = models.IntegerField(blank=True, null=True)
      email = models.EmailField()
      materias = models.ManyToManyField(Materia, verbose_name="Materias a cargo", related_name='Materias')
      dedicacion_horaria = models.IntegerField(max_length=2, blank=True, null=True)
      titulo = models.CharField(max_length=255)
      formacion_en_tics = models.CharField(max_length=2, choices=tipo_sino, default='no')

      def __unicode__(self):
         return u'%s %s' % (self.apellido, self.nombre)

      def nombre_completo(self):
         return u'%s %s' % (self.apellido, self.nombre)

      def get_materias(self):
         return "\n"+"-".join([m.nombre for m in self.materias.all()])
      get_materias.short_description = 'Materias'

      def get_tutor_de_sedes(self):
          return "\n"+"-".join([t.nombre for t in self.tutor_de_sede.all()])
      get_tutor_de_sedes.short_description = "Tutor de Sede"

      #def get_id_profesor(self):
      #    return Profesor.objects.filter(nombre='daniela')



#***************************** MODELO CALSE**********************************
class Clase(models.Model):
      profesor = models.ForeignKey(Profesor)
      tipo_clase = models.ForeignKey(TipoClase)
      nombre_de_clase = models.CharField(max_length=100, verbose_name='Nombre de la Clase', unique=True)
      usuario = models.ForeignKey(User, blank=True)

      def __unicode__(self):
         return self.nombre_de_clase
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# ************ VARIABLES ****************
tipo_genero = (
    ('hombre', 'Hombre'),
    ('mujer', 'Mujer'),
)
tipo_situacion = (
    ('padre','Padre'),
    ('madre','Madre'),
)
tipo_estado = (
    ('regular', 'Regular'),
    ('egresado', 'Egresado'),
    ('libre', 'Libre'),
    ('ex-alumno', 'Ex-Alumno'),
)
tipo_parentescos = (
    ('padre', 'Padre'),
    ('madre', 'Madre'),
    ('hermano', 'Hermano'),
    ('tia', 'Tia'),
    ('otro', 'Otro'),
)
tipo_sino = (
    ('no', 'NO'),
    ('si', 'SI'),
)
tipo_cursado = (
    ('1', '1º Año'),
    ('2', '2º Año'),
    ('3', '3º Año'),
    ('4', '4º Año'),
    ('5', '5º Año'),
)
#*********************************************************
# MODELO DE CLASES

class Sede(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Paraje")
    cue = models.CharField(max_length=10, unique=True, verbose_name="C.U.E.")
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.nombre

class Alumno(models.Model):
     nombre = models.CharField(max_length=100)
     apellido = models.CharField(max_length=50)
     dni = models.IntegerField(max_length=8, verbose_name='DNI')
     cuil = models.CharField(max_length=13, verbose_name='CUIL')
     sede = models.ForeignKey(Sede)
     genero = models.CharField(max_length=15, choices=tipo_genero)
     fecha_de_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
     edad = models.IntegerField(blank=True, null=True)
     situacion = models.CharField(max_length=20, choices=tipo_situacion, blank=True, null=True)
     discapacidad = models.CharField(max_length=2, choices=tipo_sino, default='no')
     pueblos_originarios = models.CharField(max_length=2, choices=tipo_sino, default='no')
     anio_de_ingreso = models.IntegerField(max_length=4, blank=True, null=True, verbose_name='Año de ingreso')
     asignacion_universal = models.CharField(max_length=2, choices=tipo_sino, default='no')
     activo = models.BooleanField(default=True)
     estado = models.CharField(max_length=15, choices=tipo_estado, default='Regular')
     ano_de_cursado = models.CharField(max_length=1, choices=tipo_cursado, blank=True, null=True, verbose_name='Año de cursado')
     dni_tutor = models.IntegerField(max_length=8, blank=True, null=True, verbose_name='DNI del tutor')
     nombre_tutor = models.CharField(max_length=100, blank=True, null=True)
     apellido_tutor = models.CharField(max_length=50, blank=True, null=True)
     cuil_tutor = models.CharField(max_length=13, blank=True, null=True, verbose_name='CUIL del tutor')
     parentesco = models.CharField(max_length=20, choices=tipo_parentescos, default='Madre')

     def __unicode__(self):
        return u'%s %s' % (self.apellido, self.nombre)

     def nombre_completo(self):
        return u'%s %s' % (self.apellido, self.nombre)

     def calcular_edad(self):
            hoy = timezone.now()
            ano_diferencia = hoy.year - self.fecha_de_nacimiento.year
            mes_diferencia = hoy.month - self.fecha_de_nacimiento.month
            if mes_diferencia <= 0:
                ano_diferencia = ano_diferencia - 1
            return ano_diferencia

     def save(self):
         self.edad = self.calcular_edad()
         super (Alumno, self).save()


class Coordinador(models.Model):
     nombre = models.CharField(max_length=100)
     apellido = models.CharField(max_length=50)
     dni = models.IntegerField(max_length=8, verbose_name='DNI')
     cuil = models.CharField(max_length=13, verbose_name='CUIL')
     sede = models.ForeignKey(Sede)
     direccion = models.CharField(max_length=100, blank=True, null=True)
     localidad = models.CharField(max_length=100, blank=True, null=True)
     telefono_fijo = models.IntegerField(blank=True, null=True)
     telefono_cel = models.IntegerField(blank=True, null=True)
     email = models.EmailField()
     dedicacion_horaria = models.IntegerField(max_length=2, blank=True, null=True)
     titulo = models.CharField(max_length=255)
     formacion_en_tics = models.CharField(max_length=2, choices=tipo_sino, default='no')

     def __unicode__(self):
        return u'%s %s' % (self.apellido, self.nombre)

     def nombre_completo(self):
        return u'%s %s' % (self.apellido, self.nombre)

     def obtener_id_por_nomre(nombre):
         return Coordinador.objects.get(nombre=nombre).id





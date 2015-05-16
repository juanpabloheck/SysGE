from django.db import models
from apps.sedes.models import Sede

tipo_sino = (
    ('SI', 'SI'),
    ('NO', 'NO'),
)

class Conectividad(models.Model):
    sede = models.ForeignKey(Sede)
    fecha_de_registro = models.DateField()
    hay_conectividad = models.CharField(max_length=2,choices=tipo_sino, default='SI')
    velocidad_de_subida = models.FloatField(blank=True, null=True)
    velocidad_de_bajada = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.sede.nombre

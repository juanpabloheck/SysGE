from django.db import models


class TipoClase(models.Model):
    tipo_clase = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tipo_clase

class MotivoInasistencia(models.Model):
    motivo_inasistencia = models.CharField(max_length=100)

    def __unicode__(self):
        return self.motivo_inasistencia

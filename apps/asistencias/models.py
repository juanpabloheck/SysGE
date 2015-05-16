from django.db import models
from apps.sedes.models import Alumno
from apps.configuraciones.models import MotivoInasistencia

tipo_presente = (
    ('P', 'Presente'),
    ('A', 'Ausente'),
)

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno)
    fecha = models.DateField()
    presente = models.CharField(max_length=1, choices=tipo_presente)
    motivo = models.ForeignKey(MotivoInasistencia, blank=True, null=True, default=None)


    def __unicode__(self):
        return self.alumno.nombre_completo()


class AsistenciaMasiva(Alumno):
    class Meta:
        proxy = True

from django.conf.urls import patterns, include, url
from .views import AsistenciaAlumnos

urlpatterns = patterns('',
     url(r'^asistenciaalumnos/$', AsistenciaAlumnos.as_view(), name='asistencia_alumnos'),
)


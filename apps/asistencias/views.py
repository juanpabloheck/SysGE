from django.shortcuts import render
from django.views.generic import ListView
from .models import Alumno

class AsistenciaAlumnos(ListView):
    template_name = "asistencias/asistenciaAlumnos.html"
    model = Alumno
    context_object_name = "alumnos_lista"


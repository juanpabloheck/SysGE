from django import forms
from .models import Profesor, Materia, Clase, User
from suit.widgets import NumberInput
from django.http import request
#*************************VARIABLES*********************************
tipo_titulo = (
    ('1', 'Maestro de Primaria'),
    ('2', 'Profesor de Secundaria de la Materia a su cargo'),
    ('3', 'Profesor de Secundaria de otra materia a su cargo'),
    ('4', 'Licenciado en la disciplina a su cargo'),
    ('5', 'Licenciado en otra disciplina'),
    ('6', 'Magister-Doctor'),
)

class MateriaAdminForm(forms.ModelForm):
    class Meta:
        model = Materia
        widgets = {

        }

class ProfesorAdminForm(forms.ModelForm):
    class Meta:
        model = Profesor
        widgets = {
            'titulo': forms.CheckboxSelectMultiple(choices=tipo_titulo),
            'dedicacion_horaria': NumberInput,
            'telefono_fijo': NumberInput,
            'telefono_cel': NumberInput,
        }

class ClaseAdminForm(forms.ModelForm):
    class Meta:
        model = Clase
        widgets = {
            'numero_de_clase': NumberInput
        }

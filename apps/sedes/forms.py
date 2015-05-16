from django import forms
from .models import Sede, Alumno, Coordinador
from suit.widgets import NumberInput, SuitDateWidget

#*************************VARIABLES*********************************
tipo_titulo = (
    ('1', 'Maestro de Primaria'),
    ('2', 'Profesor de Secundaria de la Materia a su cargo'),
    ('3', 'Profesor de Secundaria de otra materia a su cargo'),
    ('4', 'Licenciado en la disciplina a su cargo'),
    ('5', 'Licenciado en otra disciplina'),
    ('6', 'Magister-Doctor'),
)

#***************** CLASES FORM *********************************************

class SedeAdminForm(forms.ModelForm):
    class Meta:
        model = Sede
        widgets = {

        }

class AlumnoAdminForm(forms.ModelForm):
    class Meta:
        model = Alumno
        widgets = {
            'edad': forms.TextInput(attrs={'readonly': 'readonly'})
        }

class CoordinadorAdminForm(forms.ModelForm):
    class Meta:
        model = Coordinador
        widgets={
            'titulo': forms.CheckboxSelectMultiple( choices = tipo_titulo),
            'dedicacion_horaria': NumberInput,
            'telefono_fijo': NumberInput,
            'telefono_cel': NumberInput,
        }
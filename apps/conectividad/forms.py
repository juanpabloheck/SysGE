from django import forms
from .models import Conectividad
from suit.widgets import SuitDateWidget, LinkedSelect

class ConectividadForm(forms.ModelForm):

    class Meta:
        model = Conectividad
        widgets = {
            'fecha_de_registro': SuitDateWidget,
        }
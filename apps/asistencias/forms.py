from django import forms
from .models import Asistencia, AsistenciaMasiva
from suit.widgets import Textarea, SuitDateWidget
from django.contrib.admin import widgets
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
#*********************ASISTENCIA ********************************
class AsistenciaFormAdmin(forms.ModelForm):
    class Meta:
        model = Asistencia
        widgets = {
            'motivo_ausencia': Textarea,
            'fecha': SuitDateWidget
        }

#****************************ASISTENCIA MASIVA***************************
class AsistenciaMasivaFromAdmin(forms.ModelForm):

    class Meta:
        model = AsistenciaMasiva
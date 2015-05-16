from django import forms
from .models import Intervencion, TrabajosAprobados, Clase
from suit.widgets import Textarea, NumberInput
from smart_selects.form_fields import ChainedModelChoiceField, ModelChoiceField

class IntervencionFormAdmin(forms.ModelForm):
    class Meta:
        model = Intervencion
        widgets = {
            'observaciones': Textarea
        }

class TrabajosAprobadosFormAdmin(forms.ModelForm):
    #profesor = ModelChoiceField
    #clase = ChainedModelChoiceField(Clase, chained_field="profesor", chained_model_field="profesor", show_all=False, auto_choose=True)
    class Meta:
        model = TrabajosAprobados
        widgets = {
            'observaciones': Textarea,
            'nota_simbolica': NumberInput,
        }


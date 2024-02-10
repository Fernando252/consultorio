from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['abogado', 'cliente', 'fecha_cita', 'lugar_cita', 'descripcion']
        widgets = {
            'fecha_cita': DateTimePickerInput(),
        }
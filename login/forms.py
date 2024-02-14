from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['abogado', 'cliente', 'fecha_cita', 'lugar_cita', 'descripcion']
        widgets = {
            'abogado': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'fecha_cita': DateTimePickerInput(attrs={'class': 'form-control datetimepicker-input'}),
            'lugar_cita': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Cita, Documentos

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

   

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['caso', 'tipo_documento', 'descripcion_documento', 'archivo_adjunto']
        widgets = {
            'caso': forms.Select(attrs={'class': 'form-control'}),
            'tipo_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_documento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'archivo_adjunto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
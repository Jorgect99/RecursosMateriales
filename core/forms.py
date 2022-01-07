from django import forms
from .models import *

class ProveedorForm(forms.ModelForm):
    provedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), label='Proveedores', widget=forms.Select(attrs={
        'class': 'form-control select2'
    }))

    class Meta:
        model = Proveedor
        fields = ["provedor"]

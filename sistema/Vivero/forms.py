from django import forms
#from betterforms.multiform import MultiModelForm 
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import query_utils
from django.db.models.query import QuerySet
from Vivero.models import Departamento, Municipio, Vivero

#Create form
class FormularioDepartamento(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = ('nombre_departamento',)
        widgets = {
            'nombre_departamento': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Selecciona un departamento...'
                    
                }
            )
        }

class FormularioMunicipio(forms.ModelForm):
    
    class Meta:
        model = Municipio
        fields = ('nombre_municipio',)
        widgets = {
            'nombre_municipio': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Selecciona un municipio...'
                }
            )
        }

class FormularioVivero(forms.ModelForm):

    class Meta:
        model = Vivero
        fields = ('codigo', 'nombre_vivero','productor', 'departamento','municipio')
        widgets = {
            'departamento': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese un departamento'
                }
            ),
            'municipio': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese un municipio'
                }
            ),
            'productor': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Selecciona un productor...'
                }
            ),
            'codigo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese un codigo'
                }
            ),
            'nombre_vivero': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre'
                }
            )
        }

class DepartamentoMunicipioVivero(forms.ModelForm):
    form_classes = {
        'departamento': FormularioDepartamento,
        'municipio': FormularioMunicipio,
        'vivero': FormularioVivero,
    }
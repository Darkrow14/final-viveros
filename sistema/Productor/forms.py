from django import forms
from Productor.models import Productor
from colorfield.widgets import ColorWidget 

class FormularioProductor(forms.ModelForm):
    
    #Se crea la clase para invocar el modelo 
    class Meta:
        model = Productor 
        #fields = '__all__'

    #Se crear tuplas para guardar la información o los campos del modelo
        fields =[
            'numero_documento',
            'nombre',
            'apellido',
            'direccion',
            'email',
            'telefono',
        ]
    #Se definen las etiquetas y escribimos un diccionario

        labels = {
            'numero_documento': 'Cedula',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'direccion': 'Direccion',
            'email': 'Email',
            'telefono': 'Telefono',
        }

        widgets = {
            'numero_documento': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder':'Ingrese la cedula del productor',
                    'autofocus': 'autofocus'}),

            'nombre': forms.TextInput(
                attrs = 
                {'class': 'form-control',
                'placeholder':'Ingrese el nombre del productor', 
                'autofocus': 'autofocus'}),

            'apellido': forms.TextInput(
                attrs = 
                {'class': 'form-control',
                'placeholder':'Ingrese el apellido del productor', 
                'autofocus': 'autofocus'}),

            'direccion': forms.TextInput(
                attrs = 
                {'class': 'form-control',
                'placeholder':'Ingrese la dirección del productor', 
                'autofocus': 'autofocus'}),

            'email': forms.TextInput(
                attrs = 
                {'class': 'form-control',
                'placeholder':'Ingrese el email del productor', 
                'autofocus': 'autofocus'}),

            'telefono': forms.TextInput(
                attrs = 
                {'class': 'form-control',
                'placeholder':'Ingrese el telefono del productor', 
                'autofocus': 'autofocus'}),

            
        }


        

    
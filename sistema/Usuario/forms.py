from django import forms
from django.contrib.auth.forms import AuthenticationForm
from Usuario.models import Usuario

class FormularioUsuario(forms.ModelForm):
    """ Formulario de registro de un usuario en la BD
        Variables:
            - password1: Contraseña
            - password2: Verificación de la contraseña
    """

    password1 = forms.CharField(label= 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'requerid':'requerid',
        }
    ))

    password2 = forms.CharField(label='Contraseña de confirmacion', widget = forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña',
            'id': 'password2',
            'requerid':'requerid',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo electronico',
                }
            ),
            'nombres': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }

            ),
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            )
        }
    
    #Funcion para validar un atributo de mi formulario 
    def clean_password2(self):
        """ Validacion de contraseña
        Metodo que valida que ambas contraseñas ingresadas sean iguales, esto ants de ser encriptadas
        y guardadas en la BD, Retornar la contraseña.

        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error 
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user
        
        

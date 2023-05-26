from django.test import TestCase

from .models import Productor

# Create your tests here.
class ProductorModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Productor.objects.create(numero_documento='45343242', nombre='Juan', apellido='Perez', direccion='Cra 7 # 677', email='juan@gmail.com', telefono='123456789')
    

    def test_nombre(self):
        productor = Productor.objects.get(id = 1)
        nombre_p = productor.nombre
        self.assertEquals(nombre_p, 'Juan')
    
    def test_numero_documento(self):
        productor = Productor.objects.get(id = 1)
        numero_documento_p = productor.numero_documento
        self.assertEquals(numero_documento_p, 45343242)
    
    def test_apellido(self):
        productor = Productor.objects.get(id = 1)
        apellido_p = productor.apellido
        self.assertEquals(apellido_p, 'Perez')

    def test_direccion(self):
        productor = Productor.objects.get(id = 1)
        direccion_p = productor.direccion
        self.assertEquals(direccion_p, 'Cra 7 # 677')

    def test_email(self):
        productor = Productor.objects.get(id = 1)
        email_p = productor.email
        self.assertEquals(email_p, 'juan@gmail.com')

    def test_telefono(self):
        productor = Productor.objects.get(id = 1)
        telefono_p = productor.telefono
        self.assertEquals(telefono_p, '123456789')

        #Probar con numeros largos, nombres, caracteres no tenga nada de ello en los datos
        
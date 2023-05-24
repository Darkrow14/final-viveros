from django.test import TestCase
from .models import Vivero, Municipio, Departamento, Productor

# Create your tests here.
class ViveroModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Productor.objects.create(numero_documento='45343242', nombre='Juan', apellido='Perez', direccion='Cra 7 # 677', email='juan@gmail.com', telefono='123456789')
        Departamento.objects.create(nombre_departamento = 'Risaralda')
        Municipio.objects.create(nombre_municipio = 'Dosquebradas', departamento_id='1')
        Vivero.objects.create(nombre_vivero = 'San juan', codigo = '123', productor_id='2', departamento='1', municipio='1')


    def test_nombre_departamento(self):
        departamento = Departamento.objects.get(id=1)
        nombre_d = departamento.nombre_departamento
        self.assertEquals(nombre_d, 'Risaralda')
    
    def test_nombre_municipio(self):
        municipio = Municipio.objects.get(id =1)
        nombre_m = municipio.nombre_municipio
        self.assertEquals(nombre_m, 'Dosquebradas')
    
    def test_nombre_vivero(self):
        vivero = Vivero.objects.get(id=1)
        nombre_v = vivero.nombre_vivero
        self.assertEquals(nombre_v, 'San juan')
    
    def test_codigo_vivero(self):
        vivero = Vivero.objects.get(id=1)
        codigo_v = vivero.codigo
        self.assertEquals(codigo_v, 123)

    def test_any_vivero(self):
        
        Vivero.objects.create(nombre_vivero = 'San juan', codigo = '11233', productor_id='2', departamento='1', municipio='1')
        #value = 1
        value = 2
        assert Vivero.objects.filter(productor_id=2).count() == value, f'The amount is distinct to {value}'
         
    


    
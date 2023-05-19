from django.db import models
from Productor.models import Productor

# Create your models here.
class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'departamento'
        verbose_name_plural = 'departamentos'
    
    def __str__(self):
        return self.nombre_departamento


class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'
    
    def __str__(self):
        return self.nombre_municipio


class Vivero(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=60)
    municipio = models.CharField(max_length=60)
    codigo = models.IntegerField(unique=True)
    nombre_vivero = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'vivero'
        verbose_name_plural = 'viveros'
    
    def __str__(self):
        return self.nombre_vivero



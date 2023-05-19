from django.db import models

# Create your models here.

class Productor(models.Model):
    numero_documento = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    """numero_documento = models.IntegerField()
    numero_documento = models.IntegerField()
    numero_documento = models.IntegerField()
    numero_documento = models.IntegerField()"""
    direccion = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "productor"
        verbose_name_plural = "productores"

    
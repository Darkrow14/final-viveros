from django.db import models

from Productor.models import Productor

class finca(models.Model):
 productor:models.ForeignKey(Productor, on_delete=models.CASCADE)
 numero_catastro:models.CharField(max_length=35)
 Municipio:models.CharField(max_length=25)
 nombre_finca:models.CharField(max_length=25)

 class Meta:
        verbose_name = 'finca'
        verbose_name_plural = 'fincas'
 def __str__(self):
        return self.nombre_finca
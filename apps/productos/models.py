from django.db import models
from apps.compras.models import Compras


# Create your models here.
class products(models.Model):
    codigo = models.CharField(max_length=100)
    desccion1 = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    numero_existencia = models.CharField(max_length=100)
    
    compras = models.ManyToManyField(Compras)

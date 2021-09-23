from django.db import models
from apps.productos.models import Productos

# Create your models here.

class clients(models.model):
    nombre    = models.CharField(max_length=100)
    aepllidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    telefono  = models.CharField(max_length=100)
    producto = models.ForeignKey(Productos)


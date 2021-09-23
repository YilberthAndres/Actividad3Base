from django.db import models
from apps.productos.models import Productos

# Create your models here.
class Proveedores(models.Mmodel):
    nombre = models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=20)
    productos = models.ForeingKey(Productos)
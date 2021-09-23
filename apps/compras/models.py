from django.db import models
from apps.clients.models import Clients
from apps.productos.models import Productos


# Create your models here.
class Compras(models.Mmodel):
    fecha = models.DateField()
    registro= models.CharField(max_length=100)
    clients = models.ForeingKey(Clients)
    productos = models.Foreingkey(Productos)

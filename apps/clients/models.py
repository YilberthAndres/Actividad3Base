from django.db import models

# Create your models here.
class Clients(models.model):
    nombre    = models.CharField(max_length=100)
    aepllidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono  = models.CharField(max_length=100)


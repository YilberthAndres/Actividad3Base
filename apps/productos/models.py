from django.db import models

# Create your models here.
class Productos(models.model):
    descripcion  = models.CharField(max_length=100)
    precio       = models.BigIntegerField()
    Nexistencias = models.IntegerField()
    
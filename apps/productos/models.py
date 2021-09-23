from django.db import models


# Create your models here.
class Products(models.Model):
    codigo = models.CharField(max_length=100)
    desccion1 = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    numero_existencia = models.CharField(max_length=100)

from apps.proveedores.models import clients
from apps.productos.models import Productos
from apps.clients.models import Clients
from django.db import models

# Create your models here.



# class ventas(models.Model):
#     descripcion = models.CharField(max_length=100)
#     fechaventa = models.DateField()

class Compras(models.Model):
    descuento = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Descuento")
    subtotal  = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="sub total")
    total     = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="total")
    producto  = models.ForeignKey(Productos)
    clients   = models.ForeignKey(Clients)

from django.db import models
from .user import User
from .productos import Productos

class Carrito(models.Model):
    id_car = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='carrito', on_delete=models.CASCADE)
    prendas = models.ForeignKey(Productos, related_name='carrito', on_delete=models.CASCADE)
    subtotal = models.IntegerField(default=0)
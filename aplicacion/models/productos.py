from django.db import models
from .user import User

class Productos(models.Model):
    id_pro = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User, related_name='productos', on_delete=models.CASCADE)
    color = models.CharField('Color', max_length = 10)
    precio = models.IntegerField(default=0)
    talla = models.CharField('Talla', max_length = 3, unique=True)
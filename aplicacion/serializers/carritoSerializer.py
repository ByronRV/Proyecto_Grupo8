from aplicacion.models.carrito import Carrito
from rest_framework import serializers
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = ['id_car', 'user', 'prendas', 'subtotal']
from aplicacion.models.productos import Productos
from rest_framework import serializers
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id_pro', 'color', 'precio', 'talla']
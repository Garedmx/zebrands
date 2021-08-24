from rest_framework import serializers, viewsets
from motor.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ['id', 'name', 'sku', 'price', 'description', 'img', 'quantity', 'consulted', 'created', 'updated', 'active']






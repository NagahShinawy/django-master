from rest_framework import serializers
from .models import Product, Color


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
            "user",
        ]

    def get_discount(self, obj: Product):
        return obj.calc_discount


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            "id",
            "rgb",
            "_hexa",
        ]
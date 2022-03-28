from rest_framework import serializers
from .models import Order
from .models import Image


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "customer", "customer_telephone", "height", "width", "preview", "styles")

    def get_queryset(self):
        return self.request.Order.all()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Order.objects.create(**validated_data)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "sku", "url", "name", "category")

    def get_queryset(self):
        return self.request.Image.all()

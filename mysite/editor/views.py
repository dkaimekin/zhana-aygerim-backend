from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, Image
from .serializers import OrderSerializer, ImageSerializer


# Create your views here.


class IndexViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

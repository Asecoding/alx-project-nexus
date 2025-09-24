from django.shortcuts import render

from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class productListCreateAPIView(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = productSerializer

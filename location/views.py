from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
# Create your views here.


class CityViewAPI(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
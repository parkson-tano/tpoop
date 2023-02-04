from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.response import Response
# Create your views here.


class HouseViewAPI(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class GetHouseViewAPI(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = GetHouseSerializer


@api_view(['GET', 'PATCH'])
def search(request, city, house_type, price):
    house = House.objects.filter(Q(city=city) and Q(house_type = house_type))
    search_serializer = GetHouseSerializer(
        house, many=True, context={'request': request})
    return Response(search_serializer.data)

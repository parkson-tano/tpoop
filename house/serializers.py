from rest_framework import serializers
from .models import *
from account.serializers import GetUserSerializer


class GetHouseSerializer(serializers.ModelSerializer):
    owner = GetUserSerializer(read_only = True)
    class Meta:
        model = House
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"




from django.urls import path
from .views import *

urlpatterns = [
    path("", HouseViewAPI.as_view({'get': 'list',
                                                          'post': 'create'})),
    path("<int:pk>", GetHouseViewAPI.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
        'put' : 'update'
    })),
    path('search/<city>/<house_type>/', search),
]

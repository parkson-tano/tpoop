from django.urls import path
from .views import *

urlpatterns = [
    path("", CityViewAPI.as_view({'get': 'list',
                                            'post': 'create'})),
]

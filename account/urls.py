from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("", GetUserViewAPI.as_view({'get': 'list'}), name='user_create'),
    path("get/<int:pk>", GetUserViewAPI.as_view({'get': 'retrieve',
                                                 'patch': 'partial_update',
                                                 'delete': 'destroy'}), name='user_api'),
    path("<int:pk>", UserViewAPI.as_view({'get': 'retrieve', 'put': 'update',
                                          'patch': 'partial_update',
                                          'delete': 'destroy'}), name='user_api'),
    path('register/',
         RegisterView.as_view({'post': 'create'}), name='auth_register'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutAndBlacklistRefreshToken.as_view(), name='blacklist_token'),
    path('change_password/<str:email>/', ChangePasswordView.as_view(),
         name='auth_change_password'),
]

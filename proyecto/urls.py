from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . import aplicacion
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', aplicacion.UserCreateView.as_view()),
    path('user/<int:pk>/', aplicacion.UserDetailView.as_view()),
]

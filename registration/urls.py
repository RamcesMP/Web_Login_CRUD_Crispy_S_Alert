from django.urls import path,include
from .views import *

urlpatterns = [
    path('registro/', UserCreateView.as_view(), name='registro'),
]

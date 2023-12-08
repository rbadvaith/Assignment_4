from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_tip, name='calculate_tip'),
]

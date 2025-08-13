from django.urls import path
from . import views

# Lista de patrones URL para la aplicación dashboard
urlpatterns = [
    path('', views.index, name='dashboard_index'),
]
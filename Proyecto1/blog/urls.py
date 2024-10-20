from django.urls import path
from . import views  #Importamos las vistas de la app

urlpatterns = [
    path('', views.home, name='home'), # Define la ruta principal de la app
]
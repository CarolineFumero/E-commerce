from django.urls import path
from Clientes.views import Clientes

urlpatterns = [
    path('', Clientes, name='Clientes')
    ]
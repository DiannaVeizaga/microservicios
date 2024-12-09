from django.urls import path
from pedidosAPP.views import *
urlpatterns = [
    #la urls para registrar el pedido
    path('registrarPedido', registrarPEDIDO),
]

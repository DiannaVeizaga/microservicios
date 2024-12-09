from django.urls import path
from clientesAPP.views import *
urlpatterns = [
    #urls para las vistas
    path('estadoLOGIN', estadoLOGIN),
    path('registerCLIENTE',registrarCliente),
]

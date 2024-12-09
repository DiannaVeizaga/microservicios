from django.db import models

#modelo, o creacion de la base de datos mediante ORM
class pedidos(models.Model):
    producto = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    cliente = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
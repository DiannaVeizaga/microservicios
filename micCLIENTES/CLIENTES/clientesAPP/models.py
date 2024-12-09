"""
from django.db import models

class clientes(models.Model):
    ciCli = models.PositiveBigIntegerField(null=False)
    nombreCli = models.CharField(max_length=50)
    apellidoPaternoCli = models.CharField(max_length=50)
    emailCli = models.EmailField(max_length=30)
    passwordCli = models.CharField(max_length=30)
    """
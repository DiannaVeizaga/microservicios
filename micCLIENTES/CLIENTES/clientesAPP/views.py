from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import requests
import json
#API rest

#post
@csrf_exempt
#registrar cliente despues de obtenern los datos del otro microservicio gateway
def registrarCliente(request):
    nombreCLI = request.POST.get('nombre')
    appatCli = request.POST.get('apellido')
    usernameCli = request.POST.get('usuario')
    emailCli = request.POST.get('email')
    passwordCli = request.POST.get('contra')
    cliente = User(username = usernameCli, first_name = nombreCLI, last_name = appatCli, email=emailCli)
    cliente.set_password(passwordCli)
    cliente.save()
    return redirect('http://localhost:8000')

#login cliente, igual obtiene los datos del otro microservicio princiapl o gateway
@csrf_exempt
def estadoLOGIN(request):
    if request.method == 'POST':
        # Django ya maneja la decodificación automática del JSON en el cuerpo de la solicitud
        data = json.loads(request.body)
        user = data.get('user')
        contra = data.get('password')
        # Verificar las credenciales
        cliente = authenticate(request, username=user, password=contra)

        if cliente is not None:
            return JsonResponse({'estado': True,'usuario':user})
        else:
            return JsonResponse({'estado': False,'usuario':"no autenticado"})
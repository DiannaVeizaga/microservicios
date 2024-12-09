from django.shortcuts import render,redirect
from django.http.response import JsonResponse
import requests
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
import json

#renderizacion de platinallas
def renderPlant(request):
    return render(request, 'index.html')

def renderSesion(request):
    return render(request, 'iniciarSesion.html')

def renderRegCliente(request):
    return render(request, 'registrarCliente.html')

#vista para enviar los datos a otro microservicio para ser registrado el cliente
def registrarCliente(request):
    nombreCLI = request.POST.get('nombre')
    appatCli = request.POST.get('apellido')
    usernameCli = request.POST.get('usuario')
    emailCli = request.POST.get('email')
    passwordCli = request.POST.get('contra')
    data = {'nombre':nombreCLI,
            'apellido':appatCli,
            'usuario':usernameCli,
            'email': emailCli,
            'contra':passwordCli
            }
    response = requests.post('http://localhost:9000/registerCLIENTE',data)
    if(response.status_code==200):
        return redirect('/')
    else:
        return redirect('/register')

#login cliente, tambien comunicado con el microservicio del cliente para iniciar Sesion
def loginCliente(request):
    user = request.POST.get('username')
    contra = request.POST.get('password')
    response = requests.post(
            'http://localhost:9000/estadoLOGIN',
            json={'user': user, 'password': contra})
    
    if(response.status_code==200):
        data = response.json()
        if(data.get('estado')):
            request.session['ESTADO'] = data.get('usuario')
            return redirect('/')
        else:
            request.session['ESTADO'] = data.get('usuario')
            return redirect('/registerCLIENTE')    
    else:
        return redirect('/registerCLIENTE')

#para el js, muetsra el nombre del cliente en js
def autenticado(request):
    user = request.session.get('ESTADO')
    return JsonResponse({'user':user})

#registrarPedido, este envia datos al microservicio de pedidos para ser procesados
def registerPedido(request):
    data = json.loads(request.body)
    headers = {'Content-Type': 'application/json'}
    print(data)
    requests.post('http://localhost:10000/registrarPedido',json=data, headers=headers)
    return JsonResponse({'message':'Registro exitoso'})
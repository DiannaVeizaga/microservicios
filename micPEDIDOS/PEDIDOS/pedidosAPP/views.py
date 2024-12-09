from django.shortcuts import render
from django.http.response import JsonResponse
from pedidosAPP.models import pedidos
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
#registrar el pedido en la base de datos del mircroserivicio PEDIDOS
def registrarPEDIDO(request):
    data = json.loads(request.body) 
    print(data, "datos data")
    producto = data.get('producto')
    precio = data.get('precio')
    cliente = data.get('cliente')
    descripcion = data.get('descripcion')
    pedido = pedidos(producto=producto,
                        precio=precio,
                        cliente=cliente,
                        descripcion=descripcion
                        )
    print(pedido,"datos pedido")
    pedido.save()
    return JsonResponse({'message':"Tu pedido a sido procesado, lo recibiras muy pronto"})
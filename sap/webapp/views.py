from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from eventos.models import Cliente

# Create your views here.

def bienvenida(request):
    print('hola')
    return HttpResponse('hola')

def mostrar_clientes(request):
    cantidad_clientes = Cliente.objects.count()
    pagina = loader.get_template('Clientes.html')
    lista_clientes = Cliente.objects.all()
    datos = {'cantidad': cantidad_clientes, 'clientes': lista_clientes}

    return HttpResponse(pagina.render(datos, request))

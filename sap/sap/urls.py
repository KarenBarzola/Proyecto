"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import mostrar_clientes, bienvenida
from eventos.views import agregar_cliente, ver_cliente, editar_cliente, eliminar_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenido/',bienvenida),

    path('', mostrar_clientes, name='inicio'),
    path('agregar_cliente/', agregar_cliente),
    path('ver_cliente/<int:idCliente>', ver_cliente),
    path('editar_cliente/<int:idCliente>', editar_cliente),
    path('eliminar_cliente/<int:idCliente>', eliminar_cliente),


]

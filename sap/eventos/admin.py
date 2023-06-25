from django.contrib import admin

from eventos.models import Cliente, Tipo, Adicional

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Tipo)
admin.site.register(Adicional)


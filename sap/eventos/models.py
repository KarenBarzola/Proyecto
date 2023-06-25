from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Tipo(models.Model):
    nombre_evento = models.CharField(max_length=60, null=True)
    cantidad_personas = models.IntegerField(null=True)
    duracion = models.CharField(max_length=30, null=True)
    forma_pago = models.CharField(max_length=60, null=True)

    def __str__(self):
        return f'{self.nombre_evento}'
class Cliente(models.Model):
    PAGO = [
        ("Co", "Contado"),
        ("Cr", "Credito"),
    ]

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    pago = models.CharField(max_length=2, choices=PAGO, null=True)
    direccion = models.CharField(max_length=70)
    correo = models.CharField(max_length=60)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.id} - {self.nombre} {self.apellido}'

class Adicional(models.Model):
    DECORACION = [
        ("S", "Si"),
        ("N", "No"),
    ]

    decoracion = models.CharField(max_length=1, choices=DECORACION, null=True)
    musica = models.CharField(max_length=2, null=True)

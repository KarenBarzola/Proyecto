from django.forms import ModelForm, EmailInput

from eventos.models import Cliente

class ClienteFormulario(ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'pago', 'direccion', 'correo', 'tipo')
        widgets = {
            'correo': EmailInput(attrs={'type': 'Correo'})
        }
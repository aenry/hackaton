from django import forms
from django.forms import fields
from peoplemarket.models import Tienda , TiendaTemp

class frmTienda(forms.ModelForm):
    class Meta:
        model = TiendaTemp
        fields = ('rut', 'nombre', 'direccion', 'comuna', 'rubro')
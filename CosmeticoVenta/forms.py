from django import forms
from django.forms import ModelForm
from .models import Producto,Cliente


#para agregar los datos a laas tablas/base de datos
# + los datos que quiero agregar

#producto
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nombreProducto', 'descripcion', 'precio']

#Clientes
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['runCliente', 'nombreCompleto', 'telefono', 'gmail']
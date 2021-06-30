from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto
from .models import Cliente
from .forms import ProductoForm,ClienteForm
# Create your views here.

#aqui van todas las funciones  de nuestra pagina
def home(request):
    return render(request,'CosmeticoVenta/index.html')

def nosotros(request):
    return render(request,'CosmeticoVenta/nosotros.html')

def blog(request):
    return render(request,'CosmeticoVenta/blog.html')
 
def contact(request):
    return render(request,'CosmeticoVenta/contact.html')

def contacto(request):
    return render(request,'CosmeticoVenta/contacto.html')

def conversor_moneda(request):
    return render(request,'CosmeticoVenta/conversor_moneda.html')

def enviado(request):
    return render(request,'CosmeticoVenta/enviado.html')

def shop(request):
    return render(request,'CosmeticoVenta/shop.html')

def register(request):
    return render(request,'CosmeticoVenta/registrarvista.html')

def Clientes(request):
    return render(request,'CosmeticoVenta/Clientes.html')

def ajustes(request):
    return render(request,'CosmeticoVenta/ajustes.html')



#mostraar los datos en una tabla
def shop(request):
    listaProductos = Producto.objects.all()
    datos = {
        'productos':listaProductos,
    }
    return render(request,'CosmeticoVenta/shop.html',datos)


#funcion para ir  a la vista de agregar producto
def form_producto(request):
    datos = {
        'form':ProductoForm()
    }

    if(request.method == 'POST'):
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save() #Realiza un insert en BD
            datos['mensaje'] = 'Guardado Correctamente'
            
    return render(request,'CosmeticoVenta/form_producto.html',datos)


 #------------------------------------------------------------------------

#eliminaar el producto
def form_del_producto(request,id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()

    return redirect(to='shop')













#-----------------------------------------------------------------------------

#mostrar  los clientes en tabla
def Clientes(request):
    listaClientes = Cliente.objects.all()
    datos = {
        'cliente':listaClientes,
    }
    return render(request,'CosmeticoVenta/Clientes.html',datos)




#funcion para ir  a la vista de agregar clientes
def form_clientes(request):
    datos = {
        'form_cli':ClienteForm()
    }
    if(request.method == 'POST'):
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
            return redirect(to='home')
    return render(request,'CosmeticoVenta/form_clientes.html',datos)


#-------------------------------------------
#Modificar los clientes(Admin)
def form_mod_clientes(request, id):

    cliente = get_object_or_404(Cliente, runCliente=id)

    data = {
        'form': ClienteForm(instance=cliente)
    }
    
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente, files=request.Files)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="Clientes")
        data["form"] = formulario



    return render(request,'CosmeticoVenta/form_mod_clientes.html')


#Eliminar un Cliente registrado
def form_del_clientes(request, id):
    cliente = Cliente.objects.get(runCliente=id)
    cliente.delete()

    return redirect(to='Clientes')





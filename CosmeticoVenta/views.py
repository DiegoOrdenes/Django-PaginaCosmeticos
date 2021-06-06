from django.shortcuts import render

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
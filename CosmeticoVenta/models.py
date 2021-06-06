from django.db import models

# Create your models here.
#Modelo del producto
class Producto(models.Model):
   idProducto = models.AutoField(primary_key=True,verbose_name='Id de producto')
   nombreProducto = models.CharField(max_length=50,verbose_name='Nombre del producto')
   descripcion = models.CharField(max_length=50,verbose_name='Descripcion')
   precio = models.IntegerField(verbose_name='Precio producto')


   def __str__(self):
       return self.nombreProducto

 
#Modelo del cliente
class Cliente(models.Model):
   runCliente = models.CharField(max_length=9,primary_key=True, verbose_name='Run')
   nombreCompleto = models.CharField(max_length=20, verbose_name='NombreCompleto')
   telefono = models.IntegerField(verbose_name='Telefono')
   gmail = models.CharField(max_length=50,verbose_name='Correo electronico')
   producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
 
   def __str__(self):
       return self.runCliente

#Modelo de las ventas realizadas
class Ventas(models.Model):
    idVenta = models.IntegerField(primary_key=True,verbose_name='Venta')
    total = models.IntegerField(verbose_name='Total')
    productoA = models.ForeignKey(Cliente,on_delete=models.CASCADE)

    def __str__(self):
       return self.idVenta

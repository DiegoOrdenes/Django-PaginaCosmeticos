from django.urls import path
from .views import home
from .views import blog
from .views import contact
from .views import contacto
from .views import conversor_moneda
from .views import enviado
from .views import nosotros
from .views import shop
from .views import form_producto
from .views import register
from .views import Clientes
from .views import form_clientes
from .views import form_del_producto
from .views import form_mod_clientes
from .views import form_del_clientes
from .views import ajustes



urlpatterns = [
    path('',home,name="home"),
    path('nosotros',nosotros,name="nosotros"),
    path('blog',blog,name="blog"),
    path('shop',shop,name="shop"), 
    path('contacto',contacto,name="contacto"),
    path('conversor_moneda',conversor_moneda,name="conversor_moneda"),
    path('ajustes',ajustes,name='ajustes'),
    path('Clientes',Clientes,name="Clientes"),

    path('agregar-producto',form_producto,name='form_producto'),
    path('agregar-clientes',form_clientes,name="form_clientes"),

    path('borrar-producto/<id>',form_del_producto,name="form_del_producto"),
    
    path('modificar-cliente/<id>',form_mod_clientes,name='form_mod_clientes'),
    path('borrar-cliente/<id>',form_del_clientes,name='form_del_clientes'),

]
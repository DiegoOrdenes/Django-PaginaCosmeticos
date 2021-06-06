from django.urls import path
from .views import home
from .views import blog
from .views import contact
from .views import contacto
from .views import conversor_moneda
from .views import enviado
from .views import nosotros
from .views import shop


urlpatterns = [
    path('',home,name="home"),
    path('nosotros',nosotros,name="nosotros"),
    path('blog',blog,name="blog"),
    path('shop',shop,name="shop"), 
    path('contacto',contacto,name="contacto"),
    path('conversor_moneda',conversor_moneda,name="conversor_moneda"),
    #path('',enviado,name="enviado"),


]
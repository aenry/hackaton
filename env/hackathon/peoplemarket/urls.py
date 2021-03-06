from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('empresadata/', empresadata, name='empresadata'),
    path('agregarproducto/<id>', agregarproducto, name='agregarproducto'),
    path('seleccionarcampana/', seleccionarcampana, name='seleccionarcampana'),
    path('registrocliente/', registrocliente, name='registrocliente'),
]
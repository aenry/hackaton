from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('empresadata/', empresadata, name='empresadata'),
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
]
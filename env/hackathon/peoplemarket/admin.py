from django.contrib import admin
from django.db import models 
from .models import *


# Register your models here.
class admRubro(admin.ModelAdmin):
    list_display = ['id', 'descripcion']
    class Meta:
        model=Rubro
admin.site.register(Rubro,admRubro)

class admCategoria(admin.ModelAdmin):
    list_display = ['id', 'descripcion']
    class Meta:
        model=Categoria
admin.site.register(Categoria,admCategoria)

class admTienda(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'direccion', 'rubro']
    class Meta:
        model=Tienda
admin.site.register(Tienda,admTienda)

class admProducto(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock']
    class Meta:
        model=Producto
admin.site.register(Producto,admProducto)

class admComuna(admin.ModelAdmin):
    list_display = ['nombre', 'region']
    class Meta:
        model=Comuna
admin.site.register(Comuna,admComuna)

class admRegion(admin.ModelAdmin):
    list_display = ['nombre',]
    class Meta:
        model=Region
admin.site.register(Region,admRegion)

class admTiendaTemp(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'direccion', 'rubro']
    class Meta:
        model=TiendaTemp
admin.site.register(TiendaTemp,admTiendaTemp)
from django.db import models

# Create your models here.
class Region(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=25)
    def __str__(self):
        return str(self.nombre)

class Comuna(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=25)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nombre)

class Rubro(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=25)
    def __str__(self):
        return str(self.descripcion)

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length=25)
    def __str__(self):
        return str(self.descripcion)

class Tienda(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    logo = models.CharField(max_length=255)
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=25)
    logo = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    def __str__(self):
        return str(self.nombre)

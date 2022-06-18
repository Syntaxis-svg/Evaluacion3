from distutils.command.upload import upload
from django.db import models
from django.db.models.deletion import CASCADE

class Marca(models.Model):
    nombre = models.CharField(max_length=75)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=250)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=CASCADE)
    stock = models.IntegerField()
    def __str__(self):
        return self.nombre
    
class Gerente(models.Model):
    productomasvendido = models.CharField(max_length=75)
    productomenosvendido = models.CharField(max_length=75)
    totalproductos = models.IntegerField()

class IngresoPersonal(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField (max_length=20)
    email = models.EmailField (max_length=50)
    contraseña = models.IntegerField()
    repetircontrasena = models.IntegerField()

class Modificar_producto(models.Model):
    precio = models.IntegerField()
    stock = models.IntegerField()


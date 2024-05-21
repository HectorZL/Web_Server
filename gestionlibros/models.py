from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    
    idEstudiante=models.IntegerField()
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.CharField()
    fecharegistro=models.DateField()
    fechaultimoprestamo=models.DateField()

class Prestamos(models.Model):
    
    idPrestamo=models.IntegerField()
    idEstudiante=models.IntegerField()
    idLibro=models.IntegerField()
    FechaPrestamo=models.DateField()
    FechaDevolucion=models.DateField(default=timezone.now)
    # created =models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    
class Libros(models.Model):
    
    idPrestamo=models.IntegerField()
    nombreLibro=models.CharField(max_length=30)
    idAutor=models.IntegerField()
    idEditorial=models.IntegerField()
    nombreEditorial=models.CharField(max_length=30, default='')
    nejemplar=models.CharField(max_length=30, default='1')
    issbn=models.IntegerField(default='1')
    
class Autores(models.Model):
     idAutor=models.IntegerField()
     nombre=models.CharField(max_length=30)
     apellido=models.CharField(max_length=30)
     nacionalidad=models.CharField(max_length=30)


    
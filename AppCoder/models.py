from django.db import models

# Create your models here.

class inicio (models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()

class especialidad (models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    
class pacientes (models.Model):
    nombre = models.CharField(max_length= 35)
    apellido = models.CharField(max_length= 20)
    dni= models.IntegerField()  
    
class Profesionales (models.Model):
    nombre = models.CharField(max_length= 35)
    apellido = models.CharField(max_length= 20)
    cargo = models.CharField(max_length=15)
    email = models.EmailField(max_length=20)
    
def __str__(self):
        return f"{self.nombre} {self.apellido}"   
    
class Citas (models.Model):
    fecha = models.DateTimeField()
    turno_tomado = models.BooleanField()
    
def __str__(self):
        return f"{self.fecha} ({self.turno_tomado})"
    
class citas_Formulario (models.Model):
    nombre = models.DateTimeField()
    codigo = models.BooleanField()   
    



    
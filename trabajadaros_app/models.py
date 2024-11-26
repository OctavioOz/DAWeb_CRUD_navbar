from django.db import models

# Create your models here.

class  Trabajadores(models.Model):
    id=models.CharField(primary_key=True, max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    num_telefono=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    fecha_ne=models.DateField(max_length=50)
    fecha_ing=models.DateField(max_length=50)
    
    def __str__(self):
        return self.nombre
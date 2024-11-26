from django.db import models

# Create your models here.

class Clientes(models.Model):
    id=models.CharField(primary_key=True, max_length=10)
    nombre=models.CharField(max_length=50)
    metodo_p=models.CharField(max_length=50)
    tipo_cort=models.CharField(max_length=50)
    tipo_cab=models.CharField(max_length=50)
    fecha_nc=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
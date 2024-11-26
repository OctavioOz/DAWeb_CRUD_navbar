from django.db import models

# Create your models here.

class Venta_Productos(models.Model):
    id_venta=models.PositiveSmallIntegerField(primary_key=True)
    id_trabajador=models.PositiveSmallIntegerField()
    id_cliente=models.PositiveSmallIntegerField()
    id_producto=models.PositiveSmallIntegerField()
    fecha_venta=models.DateField()
    total=models.CharField(max_length=50)
    
    def __str__(self):
        return self.total
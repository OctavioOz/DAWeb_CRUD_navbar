from django.db import models

# Create your models here.

class Citas(models.Model):
    id_cita=models.PositiveSmallIntegerField(primary_key=True)
    id_cliente=models.PositiveSmallIntegerField()
    id_trabajador=models.PositiveSmallIntegerField()
    fecha_cita=models.DateField()
    id_corte=models.PositiveSmallIntegerField()
    total=models.CharField(max_length=50)

    def __str__(self):
        return self.total
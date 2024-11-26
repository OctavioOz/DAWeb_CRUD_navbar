from django.db import models

# Create your models here.

class Cortes(models.Model):
    id_corte=models.PositiveSmallIntegerField(primary_key=True)
    nombre_corte=models.CharField(max_length=50)
    tipo_corte=models.CharField(max_length=50)
    precio=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre_corte
    
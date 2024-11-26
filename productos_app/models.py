from django.db import models

# Create your models here.


class Prodcutos(models.Model):
    id_producto=models.PositiveSmallIntegerField(primary_key=True)
    tipo=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    olor=models.CharField(max_length=50)
    gramos=models.CharField(max_length=50)
    uso=models.CharField(max_length=50)
    precio=models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.color
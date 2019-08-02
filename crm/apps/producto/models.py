from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo_producto = models.CharField(max_length=20)
    nombre_producto = models.CharField(max_length=20)
    descripcion_producto = models.TextField(max_length=70)
    precio_producto = models.IntegerField()
    
    def __str__(self):
        return self.codigo_producto + " - " + self.nombre_producto



    

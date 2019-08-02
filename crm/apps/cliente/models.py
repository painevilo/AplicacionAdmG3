from django.db import models
from apps.localizacion.models import Region_Chile, Comuna_Chile
from datetime import datetime
# Create your models here.
class Giro_Cliente(models.Model):
    nombre_giro = models.CharField(max_length=20)
    descripcion_giro = models.TextField(max_length=70)
    def __str__(self):
        return self.nombre_giro
    
class Dependencia(models.Model):
    nombre_dependencia = models.CharField(max_length=20)
   
    def __str__(self):
        return self.nombre_dependencia

class Cliente(models.Model):
    rut =  models.CharField(max_length=20, blank = True)
    razon_social = models.CharField(max_length=50)
    giro_cliente = models.ForeignKey(Giro_Cliente,null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.razon_social

    def __str__(self):
        return self.rut


    

class Demandante(models.Model):
    id_padre = models.ForeignKey(Cliente,null=True, blank=True, on_delete=models.CASCADE)
    nombre_demandante = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(default=datetime.now())
    dependencia_demandante = models.ForeignKey(Dependencia,null=True, on_delete=models.CASCADE)
    region_demandante = models.ForeignKey(Region_Chile, blank=True, null=True, on_delete=models.CASCADE)
    comuna_demandante = models.ForeignKey(Comuna_Chile, blank=True, null=True, on_delete=models.CASCADE)
    direccion_demandante = models.CharField(max_length=50, blank = True)
    correo_demandante = models.EmailField(max_length=50, blank = True)
    telefono_demandante = models.CharField(max_length=50, blank = True)

    def __str__(self):
        return self.nombre_demandante

    def __str__(self):
        return self.id_padre.rut 

    def __str__(self):
        return self.id_padre.rut + "-" +self.nombre_demandante

    

    

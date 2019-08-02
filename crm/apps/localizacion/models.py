from django.db import models

# Create your models here.
class Region_Chile(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region =  models.CharField(max_length=50)
    ISO_3166_2_CL = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_region

class Provincia_Chile(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre_provincia =  models.CharField(max_length=50)
    id_region = models.ForeignKey(Region_Chile,null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_provincia

class Comuna_Chile(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna =  models.CharField(max_length=50)
    id_provincia = models.ForeignKey(Provincia_Chile,null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_comuna



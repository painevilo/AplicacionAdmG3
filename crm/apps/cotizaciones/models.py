from django.db import models
from apps.cliente.models import Demandante, Cliente
from apps.producto.models import Producto
from datetime import datetime
from django.contrib.auth.models import User


class Cotizacion(models.Model):
    estado_cotizaciones = (('Vendida', 'Vendida'),
              ('Pendiente', 'Pendiente'),
              ('Desierta', 'Desierta'))
    demandante = models.ForeignKey(Demandante,null=True, blank=True, on_delete=models.CASCADE)
    glosa = models.CharField(max_length=40)
    fecha_ingreso = models.DateTimeField(default=datetime.now())
    productos =  models.ManyToManyField(Producto)
    monto = models.IntegerField()
    responsable = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    estado = models.CharField(max_length=30, choices= estado_cotizaciones)

    def __str__(self):
        return self.demandante


class Historia_Cotizacion(models.Model):
    estado_cotizaciones = (('Vendida', 'Vendida'),
              ('Pendiente', 'Pendiente'),
              ('Desierta', 'Desierta'))

    tareas = (('Llamar', 'Llamar'),
              ('Re-Cotizar', 'Re-Cotizar'),
              ('Correo', 'Correo'),
              ('Visita', 'Visita'))
    id_historia = models.ForeignKey(Cotizacion,null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40,null=False, blank=False)
    fecha_ingreso = models.DateTimeField(default=datetime.now())
    responsable = models.ForeignKey(User,null=False, blank=False, on_delete=models.CASCADE)
    historia = models.TextField(max_length=100,null=False, blank=False)
    proxima_tarea = models.CharField(max_length=30, choices= tareas,null=False, blank=False)
    estado = models.CharField(max_length=30, choices= estado_cotizaciones,null=False, blank=False)
    
    def __str__(self):
        return self.id_historia.demandante 


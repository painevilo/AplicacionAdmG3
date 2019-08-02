from django.contrib import admin
from .models import Giro_Cliente, Cliente, Dependencia, Demandante
# Register your models here.

admin.site.register(Giro_Cliente)
admin.site.register(Cliente)
admin.site.register(Dependencia)
admin.site.register(Demandante)
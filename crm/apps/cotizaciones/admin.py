from django.contrib import admin

from apps.cotizaciones.models import Cotizacion, Historia_Cotizacion

# Register your models here.

admin.site.register(Cotizacion)
admin.site.register(Historia_Cotizacion)


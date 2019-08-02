from django.contrib import admin
from .models import Region_Chile, Provincia_Chile, Comuna_Chile

# Register your models here.

admin.site.register(Region_Chile)
admin.site.register(Provincia_Chile)
admin.site.register(Comuna_Chile)

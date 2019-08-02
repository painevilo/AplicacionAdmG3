from django.urls import path, re_path
from . import views 


urlpatterns = [    
    
    path('cotiRegistrar/', views.Cotizacion_Vista.as_view(), name='registro_cotizacion'),
    
   ]
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.views.generic.list import ListView
from apps.cotizaciones.forms import Cotizacion_form
from apps.cotizaciones.models import Cotizacion
from apps.cliente.views import home_genial

# Create your views here.

class Cotizacion_Vista(CreateView):
	model = Cotizacion
	template_name = 'cotizaciones/cotizacion_form.html'
	form_class = Cotizacion_form
	success_url = reverse_lazy(home_genial)





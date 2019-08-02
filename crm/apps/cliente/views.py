from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.views.generic.list import ListView
from apps.cliente.models import Giro_Cliente, Cliente, Demandante
from apps.cliente.forms import Cliente_Forms, Cliente_UpdateForms, Demandante_form,Demandante_UpdateForms


# Create your views here.

def home_genial(request):    
    return render(request, 'base/base.html', {})


class Cliente_Vista(CreateView):
	model = Cliente
	template_name = 'cliente/cliente_form.html'
	form_class = Cliente_Forms
	success_url = reverse_lazy(home_genial)

class Cliente_List(ListView):
	model = Cliente
	template_name = 'cliente/cliente_list.html'

class Cliete_Delete(DeleteView):
	model = Cliente
	template_name = 'cliente/cliente_delete.html'
	success_url = reverse_lazy('lista_cliente')
	def get_object(self):
		object = get_object_or_404(Cliente, id=self.kwargs['id'])
		return object

class Cliente_Update(UpdateView):
	model = Cliente
	template_name = 'cliente/cliente_form.html'
	form_class = Cliente_UpdateForms
	success_url = reverse_lazy('lista_cliente')
	def get_object(self):
		object = get_object_or_404(Cliente, id=self.kwargs['id'])
		return object


class Demandante_Vista(CreateView):
	model = Demandante
	template_name = 'cliente/demandante_form.html'
	form_class = Demandante_form
	success_url = reverse_lazy(home_genial)

class Demandante_List(ListView):
	model = Demandante
	template_name = 'cliente/demandante_list.html'


class Demandante_Delete(DeleteView):
	model = Demandante
	template_name = 'cliente/demandante_delete.html'
	success_url = reverse_lazy('lista_demandante')
	def get_object(self):
		object = get_object_or_404(Demandante, id=self.kwargs['id'])
		return object

class Demandante_Update(UpdateView):
	model = Demandante
	template_name = 'cliente/demandante_form.html'
	form_class = Demandante_UpdateForms
	success_url = reverse_lazy('lista_demandante')
	def get_object(self):
		object = get_object_or_404(Demandante, id=self.kwargs['id'])
		return object







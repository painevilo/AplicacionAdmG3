from django import forms

from apps.cliente.models import Giro_Cliente, Dependencia, Cliente,Demandante

class Giro_Forms(forms.ModelForm):

	class Meta:
		model = Giro_Cliente
		fields = [
			'nombre_giro',
			'descripcion_giro',	
		]
		labels = {
			'Nombre Giro': 'Número de mascotas',
			'Descripcion': 'Descripción breve',
			
		}
		widgets = {
			'nombre_giro':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion_giro':forms.Textarea(attrs={'class':'form-control'}),
		}


class Cliente_UpdateForms(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = [
			'rut',
			'razon_social',	
			'giro_cliente',
		]
		labels = {
			'Rut': 'Rut',
			'Razón Social': 'Nombre legal',
			'Giro': 'Rubro',
			
		}
		widgets = {
			'rut':forms.TextInput(attrs={'class':'form-control'}),
			'razon_social':forms.TextInput(attrs={'class':'form-control'}),
			'giro_cliente':forms.Select(attrs={'class':'form-control'}),
		}


class Cliente_Forms(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = [
			'rut',
			'razon_social',	
			'giro_cliente',
		]
		labels = {
			'Rut': 'Rut',
			'Razón Social': 'Nombre legal',
			'Giro': 'Rubro',
			
		}
		widgets = {
			'rut':forms.TextInput(attrs={'class':'form-control'}),
			'razon_social':forms.TextInput(attrs={'class':'form-control'}),
			'giro_cliente':forms.Select(attrs={'class':'form-control'}),
		}

class Demandante_form(forms.ModelForm):

	class Meta:
		model = Demandante
		fields = [
			'id_padre',
			'nombre_demandante',
			'fecha_ingreso',
			'region_demandante',
			'comuna_demandante',
			'direccion_demandante',
			'correo_demandante',
			'telefono_demandante',
		]
		labels = {
			'id_padre':'Entidad',
			'nombre_demandante':'Demandante o Sucursal',
			'fecha_ingreso':'Fecha Ingreso',
			'region_demandante':'Región',
			'comuna_demandante':'Comuna',
			'direccion_demandante':'Dirección',
			'correo_demandante':'Correo Electrónico',
			'telefono_demandante':'Télefono',
			
		}
		widgets = {
			'id_padre':forms.Select(attrs={'class':'form-control'}),
			'nombre_demandante':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_ingreso':forms.TextInput(attrs={'class':'form-control'}),
			'region_demandante':forms.Select(attrs={'class':'form-control'}),
			'comuna_demandante':forms.Select(attrs={'class':'form-control'}),
			'direccion_demandante':forms.TextInput(attrs={'class':'form-control'}),
			'correo_demandante':forms.TextInput(attrs={'class':'form-control'}),
			'telefono_demandante':forms.TextInput(attrs={'class':'form-control'}),

		}


class Demandante_UpdateForms(forms.ModelForm):

	class Meta:
		model = Demandante
		fields = [
			'id_padre',
			'nombre_demandante',
			'fecha_ingreso',
			'region_demandante',
			'comuna_demandante',
			'direccion_demandante',
			'correo_demandante',
			'telefono_demandante',
		]
		labels = {
			'id_padre':'Entidad',
			'nombre_demandante':'Demandante o Sucursal',
			'fecha_ingreso':'Fecha Ingreso',
			'region_demandante':'Región',
			'comuna_demandante':'Comuna',
			'direccion_demandante':'Dirección',
			'correo_demandante':'Correo Electrónico',
			'telefono_demandante':'Télefono',
			
		}
		widgets = {
			'id_padre':forms.Select(attrs={'class':'form-control'}),
			'nombre_demandante':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_ingreso':forms.TextInput(attrs={'class':'form-control'}),
			'region_demandante':forms.Select(attrs={'class':'form-control'}),
			'comuna_demandante':forms.Select(attrs={'class':'form-control'}),
			'direccion_demandante':forms.TextInput(attrs={'class':'form-control'}),
			'correo_demandante':forms.TextInput(attrs={'class':'form-control'}),
			'telefono_demandante':forms.TextInput(attrs={'class':'form-control'}),

		}


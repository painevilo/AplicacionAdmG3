from django import forms
from apps.cotizaciones.models import Cotizacion


class Cotizacion_form(forms.ModelForm):

	class Meta:
		model = Cotizacion
		fields = [
			'demandante',
			'glosa',
			'fecha_ingreso',
			'productos',
			'monto',
			'responsable',
			'estado',
		
		]
		labels = {
			'demandante':'Demandante',
			'glosa':'Glosa',
			'fecha_ingreso':'Fecha Ingreso',
			'productos':'productos',
			'monto':'monto',
			'responsable':'responsable',
			'estado':'estado',
			
			
		}
		widgets = {
			'demandante':forms.Select(attrs={'class':'form-control'}),
			'glosa':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_ingreso':forms.TextInput(attrs={'class':'form-control'}),
			'productos':forms.SelectMultiple(attrs={'class':'form-control'}),
			'monto':forms.TextInput(attrs={'class':'form-control'}),
			'responsable':forms.Select(attrs={'class':'form-control'}),
			'estado':forms.Select(attrs={'class':'form-control'}),
		}

from django import forms
from Apps.Docente.models import Horario, HoraEntrada, HoraSalida


class HorarioForm(forms.ModelForm):

	class Meta:
		model = Horario

		fields = [
			'h_entrada',
            'h_salida' ,
            'actividad' ,
            'f_digital',
            'observa',
		]

		labels = {
			'h_entrada': '',
            'h_salida':'' ,
            'actividad':'' ,
            'f_digital':'',
            'observa':'',

		}

		widgets = {


			'h_entrada': forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora de Entrada'}),
            'h_salida':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora de Salida'}),
            'actividad':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Actividad'}),
            'f_digital':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Firma Digital'}),
            'observa':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Observaciones'}),

		}

class HoraEntradaForm(forms.ModelForm):

	class Meta:
		model = HoraEntrada

		fields = [
			'h_entrada',

		]

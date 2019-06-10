from django import forms
from Apps.Docente.models import Categoria, Horario, HoraEntrada, HoraSalida


class HorarioForm(forms.ModelForm):

	class Meta:
		model = Horario

		fields = [
			#'h_entrada',
            #'h_salida' ,
			'date_time_entrada',
			'date_time_salida',
            'actividad' ,
            'f_digital',
            'observa',
			'iduser',

		]

		labels = {
			#'h_entrada': '',
            #'h_salida':'' ,
			'date_time_entrada':'',
			'date_time_salida':'',
            'actividad':'' ,
            'f_digital':'',
            'observa':'',
			'iduser':'',

		}

		widgets = {
			'date_time_entrada':forms.DateTimeInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora Inicial'}),
			'date_time_salida':forms.DateTimeInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora Final'}),
			#'h_entrada': forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora de Entrada'}),
            #'h_salida':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Hora de Salida'}),
            'actividad':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Actividad'}),
            'f_digital':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firma Digital'}),
            'observa':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Observaciones'}),
			'iduser':forms.Select(attrs={'class':'form-control', 'required':'', 'placeholder':'Observaciones'}),

		}

class HoraEntradaForm(forms.ModelForm):

	class Meta:
		model = HoraEntrada

		fields = [
			'h_entrada',

		]

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria

		fields = [
			'categoria',
			'idcurso',
		]
		labels = {
			'categoria':'',
			'idcurso':'Curso',
		}
		widgets = {
			'categoria':forms.TextInput(attrs={'class':'form-control', 'required':'', 'placeholder':'Categoria'}),
			'idcurso':forms.Select(attrs={'class':'form-control', 'required':'', 'placeholder':'Curso'}),
		}

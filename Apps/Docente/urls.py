from Apps.Docente.views import MarcarSalida, HorarioEscuela,MarcarEntrada, index, Cursos
from django.urls import path

app_name = 'Docente'

urlpatterns = [
    path('', index, name='index'),
    path('Curso', Cursos, name='Cursos'),
    path('Horario/<idcur>', HorarioEscuela, name='HorarioEscuela'),
    path('Marcar/Entrada/<idcur>', MarcarEntrada, name='MarcarEntrada'),
    path('Marcar/Salida/<idcur>', MarcarSalida, name='MarcarSalida'),


]

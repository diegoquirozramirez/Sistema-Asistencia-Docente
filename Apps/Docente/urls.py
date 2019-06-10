from Apps.Docente.views import  RegistroUsuario,AñadirDocente, configuracion,generar_pdf,some_view, Consolidado, Asistencia, MarcarSalida, HorarioEscuela,MarcarEntrada, index, Cursos
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'Docente'

urlpatterns = [
    path('', login_required(index), name='index'),
    path('Curso', login_required(Cursos), name='Cursos'),
    path('Horario/Marcar/<idcur>', login_required(HorarioEscuela), name='HorarioEscuela'),
    path('Marcar/Entrada/<idcur>', login_required(MarcarEntrada), name='MarcarEntrada'),
    path('Marcar/Salida/<idcur>/<idhe>', login_required(MarcarSalida), name='MarcarSalida'),
    path('Asistencia', login_required(Asistencia), name='Asistencia'),
    path('Asistencia/Consolidado', login_required(Consolidado), name='Consolidado'),
    path('Asistencia/Reporte', login_required(generar_pdf), name='Reporte'),
    path('Configuraciones', login_required(configuracion), name='Configuracion'),
    path('Configuraciones/Docente', login_required(AñadirDocente), name='AñadirDocente'),
    path('Configuraciones/Docente/Registrar', login_required(RegistroUsuario.as_view()), name='RegistrarDocente'),
]

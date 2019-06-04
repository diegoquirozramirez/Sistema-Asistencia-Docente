from django.shortcuts import render, redirect,  get_object_or_404
from Apps.Docente.models import  Horario, Categoria, HoraEntrada, HoraSalida
from Apps.Docente.forms import HorarioForm, HoraEntradaForm
from Apps.Curso.models import Curso, Ciclo
from django.http import HttpResponse,  Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
import datetime
import time
# Create your views here.
def index(request):
    return render(request, 'index.html')

#def Add_Horario(request, idcur):
#    categoria = get_object_or_404(Categoria, iduser_id=request.user.id)
#    asignatura = get_object_or_404(Curso, id=idcur)
#    if request.method == 'POST':
#        form = HorarioForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit = False)
#            post.iduser_id = request.user.id
#            h_e = datetime.datetime.strptime(post.h_entrada, '%d/%m/%Y %H:%M')
#            post.date_time_entrada = h_e
#            h_s = datetime.datetime.strptime(post.h_salida, '%d/%m/%Y %H:%M')
#            post.date_time_salida = h_s
#            post.idcurso_id = idcur
#            post.save()
#        return HttpResponseRedirect(reverse('Docente:Add_Horario', args=(str(idcur))))
#
#    else:
#        form = HorarioForm()
#    horario = Horario.objects.filter(idcurso_id=idcur)
#    contexto = {'horario':horario,'form':form, 'categoria':categoria, 'asignatura':asignatura}
#    return render(request, 'horario.html', contexto)

def HorarioEscuela(request, idcur):
    categoria = get_object_or_404(Categoria, iduser_id=request.user.id)
    asignatura = get_object_or_404(Curso, id=idcur)
    horario = Horario.objects.filter(idcurso_id=idcur)
    horaentrada = HoraEntrada.objects.last()
    horasalida = HoraSalida.objects.last()
    #calcular la tardanza llegada
    hora_escuela = Horario.objects.get(idcurso_id=idcur)
    b = hora_escuela.date_time_entrada

    diferenciaHEntrada = horaentrada.h_entrada - b
    #calcular la hora de salida excedida
    hora_escuela = Horario.objects.get(idcurso_id=idcur)
    a = hora_escuela.date_time_salida

    diferenciaHSalida = horasalida.h_salida - a

    contexto = {'horario':horario,'categoria':categoria, 'asignatura':asignatura, 'horaentrada':horaentrada, 'horasalida':horasalida,'diferenciaHEntrada':diferenciaHEntrada,'diferenciaHSalida':diferenciaHSalida}
    return render(request, 'horario.html', contexto)





def MarcarEntrada(request, idcur):
    categoria = get_object_or_404(Categoria, iduser_id=request.user.id)
    asignatura = get_object_or_404(Curso, id=idcur)
    horario = Horario.objects.filter(idcurso_id=idcur)
    hora_entrada = time.strftime("%Y/%m/%d %I:%M:%S")
    date_con = datetime.datetime.strptime(hora_entrada, '%Y/%m/%d %H:%M:%S')
    b = HoraEntrada(h_entrada=date_con, iduser_id=request.user.id, idcurso_id=idcur)
    b.save()
    return HttpResponseRedirect(reverse('Docente:HorarioEscuela', args=(str(idcur))))

def MarcarSalida(request, idcur):
    categoria = get_object_or_404(Categoria, iduser_id=request.user.id)
    asignatura = get_object_or_404(Curso, id=idcur)
    horario = Horario.objects.filter(idcurso_id=idcur)
    hora_salida = time.strftime("%Y/%m/%d %I:%M:%S")
    date_con = datetime.datetime.strptime(hora_salida, '%Y/%m/%d %H:%M:%S')
    b = HoraSalida(h_salida=date_con, iduser_id=request.user.id, idcurso_id=idcur)
    b.save()
    return HttpResponseRedirect(reverse('Docente:HorarioEscuela', args=(str(idcur))))



def Cursos(request):
    cursos = Curso.objects.filter(iduser_id=request.user.id)
    contexto = {'cursos': cursos}
    return render(request, 'cursos.html', contexto)

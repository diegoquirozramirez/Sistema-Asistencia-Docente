from django.shortcuts import render, redirect,  get_object_or_404
from Apps.Docente.models import  Categoria, Horario, Categoria, HoraEntrada, HoraSalida
from Apps.Docente.forms import HorarioForm, HoraEntradaForm
from Apps.Curso.models import Curso, Ciclo
from django.http import HttpResponse,  Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
import datetime
import time
from django.contrib.auth.models import User
### para try exceptions
from django.db import IntegrityError
from django.shortcuts import render_to_response

from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your views here.
def index(request):
    us = User.objects.filter(id=request.user.id)
    if us[0].id == 1:
        context = {'us':us}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
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

    # horario establecido por escuela
    hora_escuela = Horario.objects.get(idcurso_id=idcur)
    b = hora_escuela.date_time_entrada

    # horario establecido por escuela
    hora_escuela = Horario.objects.get(idcurso_id=idcur)
    a = hora_escuela.date_time_salida


    #Hora de Entrada
    hora_entrada = time.strftime("%Y/%m/%d")
    #hora de Salida
    hora_salida = time.strftime("%Y/%m/%d")
    #date_con = datetime.datetime.strptime(hora_entrada, '%Y/%m/%d')
    hora_marcada_entrada = HoraEntrada.objects.filter(f_entrada=hora_entrada).filter(idcurso_id=idcur) #objects.last()
    hora_marcada_salida = HoraSalida.objects.filter(id_hora_entrada__in=hora_marcada_entrada)

    contexto = {'horario':horario,'categoria':categoria, 'asignatura':asignatura,'hora_marcada_entrada':hora_marcada_entrada, 'hora_marcada_salida':hora_marcada_salida }#, 'horaentrada':horaentrada, 'horasalida':horasalida,'diferenciaHEntrada':diferenciaHEntrada,'diferenciaHSalida':diferenciaHSalida}
    return render(request, 'horario.html', contexto)


def MarcarEntrada(request, idcur):
    try:
        categoria = get_object_or_404(Categoria, iduser_id=request.user.id)
        asignatura = get_object_or_404(Curso, id=idcur)
        horario = Horario.objects.filter(idcurso_id=idcur)
        # para la hora de marcaje
        hora_entrada = time.strftime("%I:%M")
        date_con = datetime.datetime.strptime(hora_entrada, '%H:%M')
        ##############################################################
        """
        cod_entrada str
        h_entrada datetime
        h_entrada_str str
        f_entrada str
        iduser
        idcurso
        """
        #############################################################3
        #Codigo de horario de entrada
        cod_hora_entrada = time.strftime("%Y/%m/%d")
        cod_entra = datetime.datetime.strptime(cod_hora_entrada, '%Y/%m/%d')
        ####################################################################
        ################################################################
        b = HoraEntrada(cod_entrada=str(cod_entra)+str(idcur),h_entrada=date_con,f_entrada=cod_hora_entrada,h_entrada_str= hora_entrada, iduser_id=request.user.id, idcurso_id=idcur)
        b.save()
        return HttpResponseRedirect(reverse('Docente:HorarioEscuela', args=(str(idcur))))
    except IntegrityError as e:
        return HttpResponseRedirect(reverse('Docente:HorarioEscuela', args=(str(idcur))))

def MarcarSalida(request, idcur, idhe):
    try:
        categoria = get_object_or_404(Categoria, iduser_id=request.user.id)
        asignatura = get_object_or_404(Curso, id=idcur)
        horario = Horario.objects.filter(idcurso_id=idcur)
        # maracaje de salida
        hora_salida = time.strftime("%I:%M")
        date_con = datetime.datetime.strptime(hora_salida, '%H:%M')
        ###############################################################
        """
        cod_salida
        h_salida
        f_salida
        h_salida_str
        iduser
        idcurso
        """
        ###############################################################
        #codigo hora de salida
        cod_hora_salida = time.strftime("%Y/%m/%d")
        cod_sali = datetime.datetime.strptime(cod_hora_salida, '%Y/%m/%d')
        ##########################################################################
        b = HoraSalida(cod_salida=str(cod_sali)+str(idcur), h_salida=date_con,f_salida=cod_hora_salida,h_salida_str=hora_salida,id_hora_entrada_id=idhe )#iduser_id=request.user.id, idcurso_id=idcur)
        b.save()
        return HttpResponseRedirect(reverse('Docente:HorarioEscuela', args=(str(idcur))))
    except IntegrityError as e:
        return HttpResponseRedirect(reverse('Docente:HorarioEscuela', args=(str(idcur))))



def Cursos(request):
    cursos = Curso.objects.filter(iduser_id=request.user.id)
    contexto = {'cursos': cursos}
    return render(request, 'cursos.html', contexto)


def Asistencia(request):
    asistencias = HoraEntrada.objects.filter(iduser_id=request.user.id)
    asistencias_salida = HoraSalida.objects.filter(id_hora_entrada__in=asistencias)
    contexto = {'asistencias':asistencias, 'asistencias_salida': asistencias_salida}
    return render(request, 'asistencias.html', contexto)


def Consolidado(request):
    categorias = Categoria.objects.filter()
    u = User.objects.all()
    a = HoraEntrada.objects.filter(iduser__in=u)
    asistencias = HoraSalida.objects.filter(id_hora_entrada__in=a)
    categorias = Categoria.objects.filter(iduser__in=u)

    contexto = {'asistencias':asistencias, 'categorias':categorias}
    return render(request, 'Consolidado.html', contexto)

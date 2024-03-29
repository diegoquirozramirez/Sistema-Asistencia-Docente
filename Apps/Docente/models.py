from django.db import models
from django.contrib.auth.models import User
from Apps.Curso.models import Curso

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    iduser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.categoria, self.iduser)

class Horario(models.Model):
    h_entrada = models.CharField(max_length=50)
    h_salida = models.CharField(max_length=50)
    actividad = models.CharField(max_length=50)
    f_digital = models.CharField(max_length=50, blank=True)
    observa = models.CharField(max_length=50)
    date_time_entrada = models.TimeField(null=True, blank=True)
    date_time_salida = models.TimeField(null=True, blank=True)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)


    def __str__(self):
        return '{} | {} | {} | {}'.format(self.actividad, self.idcurso, self.date_time_entrada, self.date_time_salida)

class HoraEntrada(models.Model):
    cod_entrada = models.CharField(max_length=50, unique=True)
    h_entrada= models.DateTimeField(null=True, blank=True)
    f_entrada = models.CharField(null=True, blank=True, max_length=50)
    h_entrada_str = models.CharField(null=True, blank=True, max_length=50)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return '{} | {} | {} | {} '.format(self.cod_entrada, self.h_entrada, self.idcurso, self.iduser)

class HoraSalida(models.Model):
    cod_salida = models.CharField(max_length=50, unique=True)
    h_salida= models.DateTimeField(null=True, blank=True)
    f_salida = models.CharField(null=True, blank=True, max_length=50)
    h_salida_str = models.CharField(null=True, blank=True, max_length=50)
    id_hora_entrada = models.ForeignKey(HoraEntrada, on_delete=models.CASCADE)
    #iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    #idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return '{} | {} '.format(self.h_salida, self.id_hora_entrada)

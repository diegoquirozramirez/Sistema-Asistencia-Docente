from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ciclo(models.Model):
    ciclo = models.CharField(max_length=4)
    def __str__(self):
        return '{}'.format(self.ciclo)


class Curso(models.Model):
    curso = models.CharField(max_length=50)
    año = models.IntegerField()
    turno = models.CharField(max_length=50)
    aula = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    idciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{} | {} | {}'.format(self.idciclo, self.curso,  self.iduser)

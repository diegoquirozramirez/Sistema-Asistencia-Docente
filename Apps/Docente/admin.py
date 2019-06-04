from django.contrib import admin
from Apps.Docente.models import Horario, Categoria, HoraEntrada, HoraSalida
# Register your models here.
admin.site.register(Horario)
admin.site.register(HoraEntrada)
admin.site.register(HoraSalida)
admin.site.register(Categoria)

from django.contrib import admin

# Register your models here.

from .models import Alumno,Profesor,HorarioDetalle,Matricula,Curso,Asignatura

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(HorarioDetalle)
admin.site.register(Matricula)
admin.site.register(Curso)
admin.site.register(Asignatura)
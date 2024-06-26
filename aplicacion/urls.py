from django.urls import path
from . import views as v


urlpatterns = [
    path('inicio/', v.inicio, name = 'inicio'),
    path('segunda',v.segunda),
    path('gestionar/', v.gestionar, name= 'gestionar'),
    path('horario/', v.horario ),
    path('ser/', v.servicio),
    path('crear/', v.crear , name='crear'),
    path('estudiante/',v.read , name= 'read'),
    path('detail/<id_a>', v.detail , name= 'detail'),
    path('update/<id_a>', v.update , name= 'update'),
    ]
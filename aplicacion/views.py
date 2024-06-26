from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Alumno, HorarioDetalle
from aplicacion.forms import AlumnoForm,ProfesorForm
# Create your views here.



def inicio(request):
    return render(request, 'inicio.html')


def segunda(request):
    return render(request, 'segunda.html')

def gestionar(request):
    return render(request, 'gestionar.html')

def horario(request):
    lista_horario = horario.objects.all()
    return render(request, 'horario.html')
def servicio(request):
    return render(request, 'servicios.html')



def read(request):
    leer = Alumno.objects.all()
    return render(request, 'estudiantes.html', {'leer': leer})


def crear(request):
    formulario = [AlumnoForm,ProfesorForm]
    for forms in formulario:
        if request.method == 'POST':
            form = forms(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = formulario()
        return render(request, 'crear.html', {'form': form})



def detail(request, id_a):
    dele= get_object_or_404(Alumno, id_a = id_a)
    dele.delete()
    return redirect(to='read')


def update(request, id_a):
    editar= get_object_or_404(Alumno, id_a = id_a)
    form = AlumnoForm(instance=editar)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=editar)
        if form.is_valid():
            form.save()
        return redirect('read')
    return render(request,'update.html',{'form':form})



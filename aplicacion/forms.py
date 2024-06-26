from django import forms
from .models import Alumno,Profesor

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        labels = {'nom':'nombre alumno'}
        fields = ['id_a', 'nom','edad','id_curso2','cod_mat']
        
        
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'       

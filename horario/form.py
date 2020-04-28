from django import forms
from .models import Materias, Horarios


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materias
        fields = ('nombre', 'codigo', 'unidadesC')


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = ('codigo', 'seccion', 'posicion')




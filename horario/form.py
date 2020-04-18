from django import forms
from .models import Materias, PNF


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materias
        fields = ('nombre', 'codigo', 'unidadesC')


class ProfesoresForm(forms.Form):
    nombre = forms.CharField(widget=forms.Textarea)



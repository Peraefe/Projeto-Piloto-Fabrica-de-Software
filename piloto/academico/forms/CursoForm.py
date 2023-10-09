from django import forms

from ..models.base.Campus import Campus
from ..models.base.Cursos import Curso

class CursoInputForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ('nome','campus')

    #nome = forms.CharField(help_text="Nome do Curso")

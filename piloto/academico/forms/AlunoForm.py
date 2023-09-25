from django.forms import ModelForm
from django import forms

from models.base.Alunos import Aluno

class AlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = ['nomeDoAluno','cpf', 'DataNasc', 'foto', 'campus', 'curso', 'situacao', 'formaDeIngresso','matricula']
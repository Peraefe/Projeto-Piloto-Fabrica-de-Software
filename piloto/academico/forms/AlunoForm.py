from django.forms import ModelForm
from django import forms

from ..models.base.Alunos import Aluno

class AlunoInputForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('nomeDoAluno','cpf', 'dataNasc', 'foto', 'campus', 'curso', 'situacao', 'formaDeIngresso')

    # nomeDoAluno = forms.CharField(help_text="Nome Completo do Aluno")
    # cpf = forms.CharField(help_text="CPF do aluno",max_length=11,min_length=11)
    # dataNasc = forms.DateField(help_text="Data de Nascimento do Aluno")
    # foto = forms.ImageField(help_text="Foto do Aluno")
    # campus = forms.ChoiceField(help_text="Câmpus do Aluno")
    # curso = forms.ChoiceField(help_text="Curso do Aluno")
    # situacao = forms.ChoiceField(help_text="Situação do Aluno")
    # formaDeIngresso = forms.ChoiceField(help_text="Forma de Ingresso do Aluno")

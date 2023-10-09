
from django import forms

from ..models.base.Alunos import Aluno
from ..models.base.Campus import Campus
from ..models.base.Cursos import Curso
from ..models.base.choices import *

class AlunoInputForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('nomeDoAluno','cpf', 'dataNasc', 'foto', 'campus', 'curso', 'situacao', 'formaDeIngresso')

    nomeDoAluno = forms.CharField(help_text="Nome Completo do Aluno")
    cpf = forms.CharField(help_text="CPF do aluno",max_length=11,min_length=11)
    dataNasc = forms.DateField(help_text="Data de Nascimento do Aluno")
    foto = forms.ImageField(help_text="Foto do Aluno")
    # campus = forms.ChoiceField(
    #     # choices=[(campus.id, campus.nome) for campus in Campus.objects.all()],
    #     help_text="Câmpus do Aluno"
    # )
    # curso = forms.ChoiceField(
    #     # choices=[(curso.id, curso) for curso in Curso.objects.all()],
    #     help_text="Curso do Aluno"
    # )
    situacao = forms.ChoiceField(
        choices=[(0,'---------')]+[(opcao[0], opcao[1]) for opcao in OPCOES_SITUACAO],
        help_text="Situação do Aluno")
    formaDeIngresso = forms.ChoiceField(
        choices=[(0,'---------')]+[(opcao[0], opcao[1]) for opcao in OPCOES_INGRESSO],
        help_text="Forma de Ingresso do Aluno")

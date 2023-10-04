from django.views.generic import CreateView
from ..models.base.Alunos import Aluno
from django.contrib import messages
from ..forms.AlunoForm import AlunoInputForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models.base.Cursos import Curso
from ..models.base.Campus import Campus
from ..models.base.choices import *

class CreateAluno(CreateView):
    model = Aluno
    form_class = AlunoInputForm
    template_name = 'academico/cadastra_aluno.html'
    success_url = '/alunos/'

    def form_valid(self, form):
        aluno = form.save(commit=False)

        aluno.save()
        messages.success(self.request, f"Aluno {aluno.nome} cadastrado com sucesso!")
        return HttpResponseRedirect(reverse('aluno/cadastrar',  kwargs={'pk': aluno.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cursos = Curso.objects.all()
        campus = Campus.objects.all()
        situacao = OPCOES_SITUACAO
        ingresso = OPCOES_INGRESSO
        context['cursos'] = cursos
        context['campus'] = campus
        context['situacao'] = situacao
        context['ingresso'] = ingresso
        return context

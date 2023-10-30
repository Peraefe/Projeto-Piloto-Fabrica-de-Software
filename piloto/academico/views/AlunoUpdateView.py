from typing import Any
from django.db import models
from django.views.generic import UpdateView
from ..models.base.Alunos import Aluno
from ..forms.AlunoForm import AlunoInputForm
from ..models.base.Cursos import Curso
from ..models.base.Campus import Campus
from ..models.base.choices import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class UpdateAluno(LoginRequiredMixin,UpdateView):
    model = Aluno
    # form_class = AlunoInputForm
    template_name = 'academico/edita_aluno.html'
    success_url = '/alunos/'

    fields=('__all__')

    # def get_object(self):
    #     pk = self.kwargs['pk']
    #     print("pk:",pk)
    #     print("aluno:", Aluno.pk)

    #     return get_object_or_404(Aluno, pk=pk)

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

    def form_valid(self, form):
        messages.success(self.request, "Aluno editado com sucesso!")
        return super(UpdateAluno , self).form_valid(form)
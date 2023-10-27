from django.shortcuts import render
from django.http import HttpResponse
from .CursoListView import Curso
from .CampusListView import Campus
from .AlunoListView import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class HomeView(LoginRequiredMixin, View):
    template_name = 'academico/home.html'

    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        campus = Campus.objects.all()
        alunos = Aluno.objects.all()

        context = {
            'cursos': cursos,
            'campus': campus,
            'alunos': alunos,
        }

        return render(request, self.template_name, context)
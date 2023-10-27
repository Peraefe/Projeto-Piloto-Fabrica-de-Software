from typing import Any
from django.views.generic import ListView
from ..models.base.Cursos import Curso
from ..models.base.Alunos import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaCursos(LoginRequiredMixin,ListView):
    model = Curso
    template_name = 'academico/lista_cursos.html'

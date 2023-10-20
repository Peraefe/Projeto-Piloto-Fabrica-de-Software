from typing import Any
from django.views.generic import ListView
from ..models.base.Cursos import Curso
from ..models.base.Alunos import Aluno

class ListaCursos(ListView):
    model = Curso
    template_name = 'academico/lista_cursos.html'

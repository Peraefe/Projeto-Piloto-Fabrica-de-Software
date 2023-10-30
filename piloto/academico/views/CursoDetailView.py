from django.views.generic import DetailView
from ..models.base.Cursos import Curso
from django.contrib.auth.mixins import LoginRequiredMixin

class DetailCurso(LoginRequiredMixin,DetailView):
    model = Curso
    template_name = 'academico/detalhes_curso.html'

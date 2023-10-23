from django.views.generic import DetailView
from ..models.base.Cursos import Curso

class DetailCurso(DetailView):
    model = Curso
    template_name = 'academico/detalhes_curso.html'

from django.views.generic import ListView
from ..models.base.Cursos import Curso

class ListaCursos(ListView):
    model = Curso
    template_name = 'academico/include/listaCursos.html'

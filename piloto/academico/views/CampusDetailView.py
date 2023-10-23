from django.views.generic import DetailView
from ..models.base.Campus import Campus
from ..models.base.Cursos import Curso

class DetailCampus(DetailView):
    model = Campus
    template_name = 'academico/detalhes_campus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cursos = Curso.objects.all()
        context['cursos'] = cursos
        return context

from django.views.generic import DetailView

from ..models.base.Alunos import Aluno

class DetailAluno(DetailView):
    model = Aluno
    template_name = 'academico/detalhes_aluno.html'
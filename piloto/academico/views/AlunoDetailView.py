from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models.base.Alunos import Aluno

class DetailAluno(LoginRequiredMixin,DetailView):
    model = Aluno
    template_name = 'academico/detalhes_aluno.html'
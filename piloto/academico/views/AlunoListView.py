from django.views.generic import ListView
from ..models.base.Alunos import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaAlunos(LoginRequiredMixin,ListView):
    model = Aluno
    template_name = 'academico/lista_alunos.html'
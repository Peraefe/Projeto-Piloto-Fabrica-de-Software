from django.views.generic import ListView
from ..models.base.Alunos import Aluno

class ListaAlunos(ListView):
    model = Aluno
    template_name = 'lista_alunos.html'
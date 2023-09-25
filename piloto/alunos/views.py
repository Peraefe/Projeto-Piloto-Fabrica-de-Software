from django.views.generic import ListView
from .models.base.Alunos import Aluno

# Create your views here.

class ListaAlunos(ListView):
    model = Aluno
    template_name = 'lista_alunos.html'
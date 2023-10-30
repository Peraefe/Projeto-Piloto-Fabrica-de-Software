from typing import Any
from django.views.generic import ListView
from ..models.base.Cursos import Curso
from ..models.base.Alunos import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class ListaCursos(LoginRequiredMixin,ListView):
    model = Curso
    template_name = 'academico/lista_cursos.html'

    def get_queryset(self):
        result = super(ListaCursos, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Curso.objects.filter(nome__icontains=query)
            result = postresult
            if not result.exists():
                messages.error(self.request,"Curso não encontrado!!!")
        else:
            result = Curso.objects.all()
        return result
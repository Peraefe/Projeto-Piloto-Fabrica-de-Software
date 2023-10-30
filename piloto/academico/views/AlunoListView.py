from django.views.generic import ListView
from ..models.base.Alunos import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class ListaAlunos(LoginRequiredMixin,ListView):
    model = Aluno
    template_name = 'academico/lista_alunos.html'

    def get_queryset(self):
        result = super(ListaAlunos, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Aluno.objects.filter(nomeDoAluno__icontains=query)
            result = postresult
            if not result.exists():
                messages.error(self.request,"Alunos(as) não encontrados(as)!!!")
        else:
            result = Aluno.objects.all()
        return result
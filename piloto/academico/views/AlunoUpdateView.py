from django.views.generic import UpdateView
from ..models.base.Alunos import Aluno
from ..forms.AlunoForm import AlunoInputForm
from ..models.base.Cursos import Curso
from ..models.base.Campus import Campus
from ..models.base.choices import *

class UpdateAluno(UpdateView):
    model = Aluno
    form_class = AlunoInputForm
    template_name = 'academico/edita_aluno.html'
    success_url = '/alunos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cursos = Curso.objects.all()
        campus = Campus.objects.all()
        situacao = OPCOES_SITUACAO
        ingresso = OPCOES_INGRESSO
        context['cursos'] = cursos
        context['campus'] = campus
        context['situacao'] = situacao
        context['ingresso'] = ingresso
        return context

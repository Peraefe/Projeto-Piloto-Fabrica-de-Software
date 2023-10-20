from django.views.generic import CreateView
from ..models.base.Alunos import Aluno
from django.contrib import messages
from ..forms.AlunoForm import AlunoInputForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from ..models.base.Cursos import Curso
from ..models.base.Campus import Campus
from ..models.base.choices import *

class CreateAluno(CreateView):
    model = Aluno
    form_class = AlunoInputForm
    template_name = 'academico/cadastra_aluno.html'
    success_url = reverse_lazy('lista_alunos')



    #def form_valid(self, form):
    #    aluno = form.save(commit=False)
#
    #    aluno.save()
    #    messages.success(self.request, f"Aluno {aluno.nome} cadastrado com sucesso!")
    #    return HttpResponseRedirect(reverse('aluno/cadastrar',  kwargs={'pk': aluno.pk}))

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

    def form_valid(self, form):
        aluno = form.save(commit=False)
        self.save_fotoObj(aluno) if self.request.FILES.get('foto') else print(f'Sem alteração de imagem.')

        messages.success(self.request, "Aluno adicionado com sucesso!")
        return super(CreateAluno, self).form_valid(form)

    def save_fotoObj(self, aluno):

        if self.request.FILES.get('foto'):

            extensao = aluno.foto.name.split('.')[-1]
            aluno.foto.name = f'{aluno.pk}.{extensao}'


            aluno.foto.save(
                f'{aluno.pk}.{extensao}',
                aluno.foto,
                False
            )

            print(f'foto: {aluno.foto}')


        return

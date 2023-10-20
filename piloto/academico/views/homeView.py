from django.shortcuts import render
from .CursoListView import Curso
from .CampusListView import Campus
from .AlunoListView import Aluno



def home(request):
    cursos = Curso.objects.all()
    campus = Campus.objects.all()
    alunos = Aluno.objects.all()

    context = {
        'cursos': cursos,
        'campus': campus,
        'alunos': alunos,
    }

    return render(request, 'academico/home.html', context=context)
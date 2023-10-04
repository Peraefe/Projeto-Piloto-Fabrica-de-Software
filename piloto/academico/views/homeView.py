from django.shortcuts import render
from .CursoListView import Curso


def home(request):
    cursos = Curso.objects.all()

    context = {
        'cursos': cursos,
    }

    return render(request, 'academico/home.html', context=context)
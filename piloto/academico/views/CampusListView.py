from django.views.generic import ListView
from ..models.base.Campus import Campus
from ..models.base.Cursos import Curso
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaCampus(LoginRequiredMixin,ListView):
    model = Campus
    template_name = "academico/lista_campus.html"

    cursos = Curso.objects.all()

    context = {
        'cursos': cursos
    }
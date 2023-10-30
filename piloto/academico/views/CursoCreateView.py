from django.views.generic import CreateView
from django.contrib import messages
from ..forms.CursoForm import CursoInputForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models.base.Cursos import Curso
from ..models.base.Campus import Campus
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateCurso(LoginRequiredMixin,CreateView):
    model = Curso
    form_class = CursoInputForm
    template_name = 'academico/cadastra_curso.html'
    success_url = '/cursos/'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cursos = Curso.objects.all()
        campus = Campus.objects.all()
        context['cursos'] = cursos
        context['campus'] = campus
        return context

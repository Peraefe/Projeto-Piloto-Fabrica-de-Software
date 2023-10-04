#academico/urls.py

from django.urls import path
from .views.AlunoListView import ListaAlunos
from .views.CursoListView import ListaCursos
from .views.homeView import home
from .views.AlunoCreateView import CreateAluno


urlpatterns = [
    path('alunos/', ListaAlunos.as_view(), name='lista_alunos'),
    path('alunos/cadastrar/', CreateAluno.as_view(), name='cadastra_alunos'),
    path('cursos/',ListaCursos.as_view(),name='lista_cursos'),
    path('', home,name='home'),
]
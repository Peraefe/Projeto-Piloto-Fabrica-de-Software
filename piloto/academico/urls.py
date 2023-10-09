#academico/urls.py

from django.urls import path
from .views.AlunoListView import ListaAlunos
from .views.CursoListView import ListaCursos
from .views.CampusListView import ListaCampus
from .views.homeView import home
from .views.AlunoCreateView import CreateAluno
from .views.AlunoUpdateView import UpdateAluno
from .views.CursoCreateView import CreateCurso

urlpatterns = [
    path('alunos/', ListaAlunos.as_view(), name='lista_alunos'),
    path('alunos/cadastrar/', CreateAluno.as_view(), name='cadastra_alunos'),
    path('alunos/editar/<int:pk>/', UpdateAluno.as_view(), name='edita_aluno'),
    path('cursos/',ListaCursos.as_view(),name='lista_cursos'),
    path('cursos/cadastrar/', CreateCurso.as_view(), name='cadastra_cursos'),
    path('campus/',ListaCampus.as_view(),name='lista_campus'),
    path('', home,name='home'),
]
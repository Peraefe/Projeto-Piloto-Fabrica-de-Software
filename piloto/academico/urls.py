#academico/urls.py
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views.AlunoListView import ListaAlunos
from .views.CursoListView import ListaCursos
from .views.CampusListView import ListaCampus
from .views.homeView import home
from .views.AlunoCreateView import CreateAluno
from .views.AlunoDetailView import DetailAluno
from .views.AlunoUpdateView import UpdateAluno
from .views.CursoCreateView import CreateCurso

urlpatterns = [
    path('alunos/', ListaAlunos.as_view(), name='lista_alunos'),
    path('alunos/cadastrar/', CreateAluno.as_view(), name='cadastra_alunos'),
    path('alunos/<int:pk>', DetailAluno.as_view(), name='detalhes_aluno'),
    path('alunos/editar/<int:pk>', UpdateAluno.as_view(), name='edita_aluno'),
    path('cursos/',ListaCursos.as_view(),name='lista_cursos'),
    path('cursos/cadastrar/', CreateCurso.as_view(), name='cadastra_cursos'),
    path('campus/',ListaCampus.as_view(),name='lista_campus'),
    path('', home,name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
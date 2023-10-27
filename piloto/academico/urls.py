#academico/urls.py
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views.AlunoListView import ListaAlunos
from .views.CursoListView import ListaCursos
from .views.CampusListView import ListaCampus
from .views.HomeView import HomeView
from .views.loginView import LoginView
from django.contrib.auth.views import LogoutView
from .views.AlunoCreateView import CreateAluno
from .views.AlunoDetailView import DetailAluno
from .views.AlunoUpdateView import UpdateAluno
from .views.CursoCreateView import CreateCurso
from .views.CursoDetailView import DetailCurso
from .views.CampusDetailView import DetailCampus

urlpatterns = [
    path('alunos/', ListaAlunos.as_view(), name='lista_alunos'),
    path('alunos/cadastrar/', CreateAluno.as_view(), name='cadastra_alunos'),
    path('alunos/<int:pk>', DetailAluno.as_view(), name='detalhes_aluno'),
    path('alunos/editar/<int:pk>', UpdateAluno.as_view(), name='edita_aluno'),
    path('cursos/',ListaCursos.as_view(),name='lista_cursos'),
    path('cursos/cadastrar/', CreateCurso.as_view(), name='cadastra_cursos'),
    path('cursos/<int:pk>', DetailCurso.as_view(), name='detalhes_curso'),
    path('campus/',ListaCampus.as_view(),name='lista_campus'),
    path('campus/<int:pk>', DetailCampus.as_view(), name='detalhes_campus'),
    path('home', HomeView.as_view(),name='home'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
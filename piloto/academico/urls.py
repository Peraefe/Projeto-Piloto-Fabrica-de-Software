#academico/urls.py

from django.urls import path
from .views.AlunoListView import ListaAlunos

urlpatterns = [
    path('alunos/', ListaAlunos.as_view(), name='lista_alunos')
]
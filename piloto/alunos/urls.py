#alunos/urls.py

from django.urls import path
from .views import ListaAlunos

urlpatterns = [

    path('aluno/', ListaAlunos.as_view(), name = 'lista_alunos')
]
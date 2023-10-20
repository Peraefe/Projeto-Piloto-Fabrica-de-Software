from django.db import models
from .Alunos import Aluno
from .Cursos import Curso

class Campus(models.Model):

    nome = models.CharField('Nome do Câmpus', max_length = 50, unique = True)

    class Meta:
        verbose_name = "Câmpus"
        verbose_name_plural = "Câmpus"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def retornaAlunosNoCampus(self):
        alunos = Aluno.objects.filter(campus = self, situacao = 4).count()
        return alunos

    def retornaCursosNoCampus(self):
        cursos = Curso.objects.filter(campus = self).count()
        print("cursos:",cursos)
        return cursos
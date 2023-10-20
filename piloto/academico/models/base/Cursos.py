from django.db import models
from ..base.Alunos import Aluno

class Curso(models.Model):

    nome = models.CharField('Nome do Curso', max_length = 100)
    campus = models.ForeignKey("Campus", on_delete=models.CASCADE, verbose_name='Câmpus')



    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']


    def __str__(self):
        return '{0} - {1}'.format(
            self.nome,
            self.campus
        )

    def retornaAlunosCursando(self):
        alunos = Aluno.objects.filter(curso=self, situacao = 4).count()
        return alunos
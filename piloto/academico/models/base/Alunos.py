from django.db import models
import datetime
from .choices import *

def diretorio_imagens_aluno(instance, filename):
    return 'fotos/(0)/(1)'.format(instance.id, filename)


class Aluno(models.Model):

    nomeDoAluno = models.CharField('Nome do Aluno', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    dataNasc = models.DateField('Data de Nascimento')
    foto = models.ImageField(upload_to=diretorio_imagens_aluno, blank=True, null=True)
    campus = models.ForeignKey('Campus', on_delete = models.SET_NULL, null = True)
    curso = models.ForeignKey('Curso', on_delete = models.SET_NULL, null = True)
    situacao = models.SmallIntegerField('Situação',choices=OPCOES_SITUACAO)
    formaDeIngresso= models.SmallIntegerField('Forma de Ingresso',choices=OPCOES_INGRESSO)
    matricula = models.CharField('Matrícula', max_length=9, unique=True, editable=False)

    def __str__(self):
        return '{0} - {1}'.format(
            self.nomeDoAluno,
            self.matricula
        )

    def generate_matricula(self):
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        semestre = '1' if month < 6 else '2'

        ultima_matricula = Aluno.objects.order_by('-matricula').first()

        if ultima_matricula:
            ultima_matricula = ultima_matricula.matricula
            if int(ultima_matricula[4]) != int(semestre) or int(ultima_matricula[0:4]) != int(year):
                proximo_numero = 1
            else:
                ultimo_numero = int(ultima_matricula[5:9])
                proximo_numero = ultimo_numero + 1
        else:
            proximo_numero = 1

        matricula = f"{year}{semestre}{proximo_numero:04d}"

        return matricula

    def save(self, *args, **kwargs):
        if not self.matricula:
            self.matricula = self.generate_matricula()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['nomeDoAluno']

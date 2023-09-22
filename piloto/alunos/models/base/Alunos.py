from django.db import models
import datetime
from .choices import *

def diretorio_imagens_aluno(instance, filename):
    return 'fotos/(0)/(1)'.format(instance.id, filename)

id = 0

def generate_matricula():
    global id
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    semestre = '1' if month < 6 else '2'

    matricula = f"{year}{semestre}{id:04d}"

    id += 1

    return matricula

class Aluno(models.Model):

    nomeDoAluno = models.CharField('Nome do Aluno', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    dataNasc = models.DateField('Data de Nascimento')
    foto = models.ImageField(upload_to=diretorio_imagens_aluno, blank=True) #adicionar upload_to
    curso = models.SmallIntegerField('Curso',choices=OPCOES_CURSOS)
    campus = models.SmallIntegerField('Câmpus',choices=OPCOES_CAMPUS)
    situacao = models.SmallIntegerField('Situação',choices=OPCOES_SITUACAO)
    formaDeIngresso= models.SmallIntegerField('Forma de Ingresso',choices=OPCOES_INGRESSO)
    matricula = models.CharField('Matrícula',max_length=10, default=generate_matricula, unique=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['nomeDoAluno']

    def __str__(self):
        return '{0} - {1}'.format(
            self.nomeDoAluno,
            self.matricula,
            self.campus,
            self.curso
        )

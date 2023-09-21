from django.db import models

class Aluno(models.Model):

    nomeDoAluno = models.CharField('Nome do Aluno', max_length=100)
    cpf = models.CharField('Cpf', max_length=11)
    matricula = models.CharField('Matricula', max_length=9) #AutoField + year , vai pensando
    dataNasc = models.DateField('Data de Nascimento')
    foto = models.ImageField('Foto do Aluno') #adicionar upload_to
    curso = models.CharField('Curso', max_length=50) #mudar para choices
    campus = models.CharField('Campus', max_length=20) #tbm
    situacao = models.CharField('Situação') #tbm
    formaDeIngresso= models.CharField('Forma de Ingresso') #tbm


    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ['Nome do Aluno']

    def __str__(self):
        return self.nomeDoAluno

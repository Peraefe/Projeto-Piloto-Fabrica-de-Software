from django import template

register = template.Library()

from ..models.base.Cursos import Curso
from ..models.base.Alunos import Aluno


@register.simple_tag
def retornaQtdAlunosCursoPorSituacao(curso, situacao=None):
    if situacao==None :
        return Aluno.objects.filter(curso = curso).count()
    else:
        return Aluno.objects.filter(curso = curso, situacao = situacao).count()


@register.simple_tag
def retornaAlunosPorSituacao(situacao=None):
    if situacao==None :
        return Aluno.objects.all().count()
    else:
        return Aluno.objects.filter(situacao = situacao).count()

@register.simple_tag
def retornaQtdAlunosCampusPorSituacao(campus,situacao=None):
    if situacao==None :
        return Aluno.objects.filter(campus = campus).count()
    else:
        return Aluno.objects.filter(campus = campus, situacao = situacao).count()

@register.simple_tag
def retornaCursosNoCampus(campus):
    cursos = Curso.objects.filter(campus = campus).count()
    return cursos

from django.contrib import admin
from .models.base.Alunos import Aluno

# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomeDoAluno', 'matricula', 'cpf', 'campus', 'curso', 'situacao', 'formaDeIngresso' )

admin.site.register(Aluno, AlunoAdmin)

from django.contrib import admin
from .models.base.Alunos import Aluno
from .models.base.Campus import Campus
from .models.base.Cursos import Curso

# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomeDoAluno', 'matricula', 'cpf', 'campus', 'curso', 'situacao', 'formaDeIngresso' )
    readonly_fields = ['foto_preview']

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'campus')


admin.site.register(Curso,CursoAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Campus)

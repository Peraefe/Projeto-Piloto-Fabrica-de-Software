from django.contrib import admin
from .models.base.Cursos import Curso

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'campus')

admin.site.register(Curso,CursoAdmin)
from django.db import models

class Curso(models.Model):

    nome = models.CharField('Nome do Curso', max_length = 100)
    campus = models.ForeignKey("campus.Campus", on_delete=models.CASCADE, verbose_name='Câmpus')



    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']


    def __str__(self):
        return '{0} - {1}'.format(
            self.nome,
            self.campus
        )
from django.db import models

class Campus(models.Model):

    nome = models.CharField('Nome do Câmpus', max_length = 50, unique = True)

    class Meta:
        verbose_name = "Câmpus"
        verbose_name_plural = "Câmpus"
        ordering = ['nome']

    def __str__(self):
        return self.nome
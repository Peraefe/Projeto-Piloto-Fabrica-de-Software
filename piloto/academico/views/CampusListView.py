from django.views.generic import ListView
from ..models.base.Campus import Campus

class ListaCampus(ListView):
    model = Campus
    template_name = "academico/lista_campus.html"
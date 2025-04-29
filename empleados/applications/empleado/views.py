from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from .models import Empleado

class IndexView (TemplateView) :
    template_name = 'home/index.html'
# Create your views here.
class PruebaListaView (ListView) :
    template_name = 'home/lista.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'


class ModeloPruebaListView(ListView):
    model = Empleado
    template_name = 'home/lista-prueba.html'
    queryset = Empleado.objects.all()
    context_object_name = 'lista_prueba'
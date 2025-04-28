from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from .models import empleado

class IndexView (TemplateView) :
    template_name = 'home/index.html'
# Create your views here.
class pruebaListaView (ListView) :
    template_name = 'home/lista.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'


class ModeloPruebaListView(ListView):
    model = empleado
    template_name = 'home/lista-prueba.html'
    context_object_name = 'lista_prueba'
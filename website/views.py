from django.shortcuts import render
from .models import Sobre, Especialidades, Depoimentos, Equipe
from django.views.generic import ListView, DetailView


class ContextoPadraoMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidade_list'] = Especialidades.objects.all()
        context['equipe_list'] = Equipe.objects.all()
        return context
  

class HomeListView(ContextoPadraoMixin, ListView):
    model = Sobre
    template_name = 'index.html'

class SobreListView(ContextoPadraoMixin, ListView):
    model = Sobre
    template_name = 'quem_somos.html'
    context_object_name = 'sobre_list'

class EspecialidadesListView(ContextoPadraoMixin, ListView):
    model = Especialidades
    template_name = 'especialidades.html'

class EspecialidadeDetailView(ContextoPadraoMixin, DetailView):
    model = Especialidades
    template_name = 'especialidade_detail.html'
    context_object_name = 'especialidade'

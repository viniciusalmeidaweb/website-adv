from django.shortcuts import render
from .models import Sobre, Especialidades, Depoimentos, Equipe
from django.views.generic import ListView, DetailView


class HomeListView(ListView):
    model = Sobre
    template_name = 'index.html' # Template onde será renderizada a view
    context_object_name = 'sobre_list'  # O nome que o objeto terá no template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Adiciona as especialidades
        context['especialidade_list'] = Especialidades.objects.all()  # O nome que o objeto terá no template
        
        # Adiciona a equipe
        context['equipe_list'] = Equipe.objects.all()  # O nome que o objeto terá no template

        return context
    
      
class EspecialidadeDetailView(DetailView):
    model = Especialidades
    template_name = 'especialidade_detail.html' # Template onde será renderizada a view
    context_object_name = 'especialidade'  # O nome que o objeto terá no template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        especialidades_lista = Especialidades.objects.all()  # Aqui, você pode adicionar qualquer outro queryset
        context['especialidade_lista_itens'] = especialidades_lista  # O nome que o objeto terá no template
        return context


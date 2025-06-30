from django.shortcuts import render
from .models import Sobre, Especialidades, Depoimentos, Equipe, Post, Categoria
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContatoForm


class ContextoPadraoMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidade_list'] = Especialidades.objects.all()
        context['equipe_list'] = Equipe.objects.all()
        context['categoria_list'] = Categoria.objects.all()
        return context
  

class HomeListView(ContextoPadraoMixin, ListView):
    model = Sobre
    template_name = 'index.html'


class BlogListView(ContextoPadraoMixin, ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(publicado=True).order_by('-data_criacao')
    
  
class BlogDetailView(ContextoPadraoMixin, DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post_detail'

    def get_object(self):
        categoria_slug = self.kwargs['categoria_slug']
        post_slug = self.kwargs['post_slug']
        return get_object_or_404(Post, slug=post_slug, categoria__slug=categoria_slug)


class CategoriaDetailView(ContextoPadraoMixin, ListView):
    model = Post
    template_name = 'categoria_detail.html'
    context_object_name = 'category_post'

    def get_queryset(self):
        categoria_slug = self.kwargs['slug']
        self.categoria = get_object_or_404(Categoria, slug=categoria_slug)
        return Post.objects.filter(categoria__slug=categoria_slug)  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # ← chama ContextoPadraoMixin + ListView
        context['categoria'] = self.categoria          # ← adiciona só o que é específico da view
        return context

    
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


class ContatoView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')  # Redireciona após o envio

    def form_valid(self, form):
        # Aqui você pode enviar email, salvar no banco, etc.
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        telefone = form.cleaned_data['telefone']
        mensagem = form.cleaned_data['mensagem']

        # Exemplo: imprimir no console
        print(f"Mensagem de {nome}, {telefone}, <{email}>: {mensagem}")

        return super().form_valid(form)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os
from website.views import HomeListView, SobreListView, EspecialidadesListView, EspecialidadeDetailView, BlogListView, BlogDetailView, ContatoView, CategoriaDetailView
from website.sitemaps import (StaticViewSitemap, CategoriaSitemap, PostSitemap, EspecialidadeSitemap)
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'categorias': CategoriaSitemap,
    'posts': PostSitemap,
    'especialidades': EspecialidadeSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    # Página inicial
    path('', HomeListView.as_view(), name="home"), 
  
      
    # Blog - Categorias (mais específico vem primeiro)
    path('blog/categoria/<slug:slug>/', CategoriaDetailView.as_view(), name='categoria_detail'),

    # Blog - Detalhe do post (rota mais genérica vem depois)
    path('blog/<slug:categoria_slug>/<slug:post_slug>/', BlogDetailView.as_view(), name="post_detail"), 

    # Blog - Lista geral
    path('blog/', BlogListView.as_view(), name="blog"), 

    # Páginas estáticas
    path('quem-somos/', SobreListView.as_view(), name="sobre"),
    path('especialidades/', EspecialidadesListView.as_view(), name="especialidades"),
    path('especialidade/<slug:slug>/', EspecialidadeDetailView.as_view(), name='especialidade_detail'),
    path('contato/', ContatoView.as_view(), name="contatos"), 

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










#Você não pode passar a mesma rota pra duas views diferentes
#Se na rota você quer exibir informações de especialidade, serviços, quem somos. Você deve passar eles todos no contexto de uma única view que utiliza essa rota
    #E não um contexto em cada view. Se não dá BO. O django vai usar a primeira view qye consome aquela rota, Que no caso é home
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Categoria, Especialidades
from datetime import datetime


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home', 'sobre', 'especialidades', 'contatos']

    def location(self, item):
        return reverse(item)


class EspecialidadeSitemap(Sitemap):
    priority = 0.7
    changefreq = 'monthly'

    def items(self):
        return Especialidades.objects.all()

    def location(self, obj):
        return reverse('especialidade_detail', args=[obj.slug])


class CategoriaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Categoria.objects.all()

    def location(self, obj):
        return reverse('categoria_detail', args=[obj.slug])


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.filter(publicado=True)

    def location(self, obj):
        return reverse('post_detail', args=[obj.categoria.slug, obj.slug])

    def lastmod(self, obj):
        return obj.data_criacao or datetime.now()

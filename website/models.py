from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.utils.text import Truncator
from django.utils.html import strip_tags


# Create your models here.
class Sobre(models.Model):
    id = models.AutoField(primary_key=True)
    quemsomos = models.TextField(default="Escreva sobre a empresa", null=True)

    class Meta:
        verbose_name = "Quem Somos"
        verbose_name_plural = "Quem Somos"

    def __str__(self):
        return self.quemsomos
    

class Especialidades(models.Model):
    id = models.AutoField(primary_key=True)
    icone = models.ImageField(upload_to='media/icones/', blank=True, null=True)
    nome_especialidade = models.CharField(max_length=100, blank=True,null=True)
    slug = AutoSlugField(populate_from='nome_especialidade', unique=True, null=True, blank=True)
    descricao_especialidade = HTMLField()  # TinyMCE será aplicado aqui
    resumo_especialidade = models.CharField(max_length=255, blank=True, null=True) 

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nome_especialidade

class Depoimentos(models.Model):
    id = models.AutoField(primary_key=True)
    cliente_depoimento = models.CharField(max_length=100, blank=True, null=True)
    depoimento = models.TextField(default="Escreva seu depoimento", null=True)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return self.depoimento

class Equipe(models.Model):
     id = models.AutoField(primary_key=True)
     nome_adv = models.CharField(max_length=100)
     photo = models.ImageField(upload_to='website/', blank=True, null=True)
     perfil_adv = models.TextField(default="Escreva seu perfil")
     
     class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipe"
        
     def __str__(self):
         return self.nome_adv
     

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(unique=True, null=True, blank=True, populate_from='nome')

    def __str__(self):
        return self.nome
    
    

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    photo_blog = models.ImageField(upload_to='blog/', blank=True, null=True)
    slug = AutoSlugField(populate_from='titulo', unique=True, null=True, blank=True, max_length=200)
    conteudo = HTMLField()  # TinyMCE será aplicado aqui
    data_criacao = models.DateTimeField(default=timezone.now)
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    @property
    def resumo(self):
        texto_limpo = strip_tags(self.conteudo)  # remove HTML
        return Truncator(texto_limpo).words(20, truncate='...')  # limita caracteres
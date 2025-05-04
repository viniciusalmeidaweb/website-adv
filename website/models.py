from django.db import models
from tinymce.models import HTMLField

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
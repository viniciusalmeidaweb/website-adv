from django.db import models

# Create your models here.
class Sobre(models.Model):
    id = models.AutoField(primary_key=True)
    quemsomos = models.TextField(default="Escreva sobre a empresa", null=True)

    def __str__(self):
        return self.quemsomos
    

class Especialidades(models.Model):
    id = models.AutoField(primary_key=True)
    nome_especialidade = models.CharField(max_length=100, blank=True,null=True)
    descricao_especialidade = models.TextField(default="Escreva sobre a especialidade", null=True)

    def __str__(self):
        return self.nome_especialidade

class Depoimentos(models.Model):
    id = models.AutoField(primary_key=True)
    cliente_depoimento = models.CharField(max_length=100, blank=True, null=True)
    depoimento = models.TextField(default="Escreva seu depoimento", null=True)

    def __str__(self):
        return self.depoimento

class Equipe(models.Model):
     id = models.AutoField(primary_key=True)
     nome_adv = models.CharField(max_length=100)
     photo = models.ImageField(upload_to='website/', blank=True, null=True)
     perfil_adv = models.TextField(default="Escreva seu perfil")

     def __str__(self):
         return self.nome_adv
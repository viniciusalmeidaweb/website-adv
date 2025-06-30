from django.contrib import admin
from website.models import Sobre, Especialidades,Depoimentos,Equipe, Post, Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug') 

class SobreAdmin(admin.ModelAdmin):
    list_display = ('quemsomos',) 

class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'conteudo', 'categoria', 'data_criacao',)

class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('nome_especialidade','slug','descricao_especialidade','icone',)
    
class DepoimentosAdmin(admin.ModelAdmin):
     list_display = ('cliente_depoimento', 'depoimento',)
   
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome_adv','perfil_adv',)


admin.site.register(Sobre, SobreAdmin)
admin.site.register(Especialidades, EspecialidadesAdmin)
admin.site.register(Depoimentos, DepoimentosAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Post)
admin.site.register(Categoria)

from django.contrib import admin
from website.models import Sobre, Especialidades,Depoimentos,Equipe

# Register your models here.
class SobreAdmin(admin.ModelAdmin):
    list_display = ('quemsomos',) 

class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('especialidade','descricao_especialidade',)
    
class DepoimentosAdmin(admin.ModelAdmin):
     list_display = ('cliente_depoimento', 'depoimento',)
   
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome_adv','perfil_adv',)


admin.site.register(Sobre, SobreAdmin)
admin.site.register(Especialidades, EspecialidadesAdmin)
admin.site.register(Depoimentos, DepoimentosAdmin)
admin.site.register(Equipe, EquipeAdmin)

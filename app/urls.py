from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website.views import HomeListView, SobreListView, EspecialidadesListView, EspecialidadeDetailView, BlogListView, BlogDetailView, ContatoView


urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', HomeListView.as_view(), name="home"), 
    path('blog/', BlogListView.as_view(), name="blog"), 
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name="post_detail"), 
    path('quem-somos/', SobreListView.as_view(), name="sobre"),
    path('especialidades/', EspecialidadesListView.as_view(), name="especialidades"),
    path('especialidade/<slug:slug>/', EspecialidadeDetailView.as_view(), name='especialidade_detail'),
    path('contato/', ContatoView.as_view(), name="contatos"), 

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










#Você não pode passar a mesma rota pra duas views diferentes
#Se na rota você quer exibir informações de especialidade, serviços, quem somos. Você deve passar eles todos no contexto de uma única view que utiliza essa rota
    #E não um contexto em cada view. Se não dá BO. O django vai usar a primeira view qye consome aquela rota, Que no caso é home
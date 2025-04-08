
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from website.views import HomeListView, EspecialidadeDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeListView.as_view(), name="sobre"), 
    path('especialidade/<int:pk>/', EspecialidadeDetailView.as_view(), name='especialidade_detail'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










#Você não pode passar a mesma rota pra duas views diferentes
#Se na rota você quer exibir informações de especialidade, serviços, quem somos. Você deve passar eles todos no contexto de uma única view que utiliza essa rota
    #E não um contexto em cada view. Se não dá BO. O django vai usar a primeira view qye consome aquela rota, Que no caso é home
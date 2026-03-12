from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.CadastrarUsuario.as_view(),name='cadastro'),
    path('listar_usuarios',views.ListarUsuario.as_view(),name='listar'),
    path('usuario/<int:pk>/atualizar',views.UpdateUsuario.as_view(),name='update'),
    path('usuario/<int:pk>/deletar',views.DeleteUsuario.as_view(),name='deletar')
    

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # para acessar midias via url.

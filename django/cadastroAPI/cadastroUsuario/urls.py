from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.cadastrar_usuario.as_view(), name='cadastro'),
    path('listar_usuarios',views.ListarUsuarios.as_view(),name='listar'),
    path('usuarios/<int:pk>/atualizar/', views.UsuarioUpdate.as_view(), name='atualizar'),
    path('deletar_usuario/<int:pk>/',views.DeletarUsuario.as_view(), name ='deletar')


   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
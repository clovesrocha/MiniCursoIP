from django.contrib import admin
from django.urls import path,include # Por padrão virá importando só o path, adicione o include.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Usuario.urls')) # urls do app que você criou
]

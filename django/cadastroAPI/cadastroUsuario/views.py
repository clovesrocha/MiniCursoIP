from django.shortcuts import render,redirect,get_object_or_404
from .models import Usuario
from django.urls import reverse
from django.core import serializers
from .serializers import UsuarioSerializer,UsuarioUpdateSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status,generics
from django.views.decorators.csrf import csrf_exempt


class cadastrar_usuario(generics.CreateAPIView):
    serializer_class=UsuarioSerializer

    def get(self,request, *args, **kwargs):

        serializer = self.serializer_class()
        return render(request,'cadastrar_usuario.html', {'serializer':serializer})
    
    def post (self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            serializer.save()
            return redirect('cadastro')
        else: 
             return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)
    
class ListarUsuarios(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        usuarios = self.get_queryset()
        return render(request, 'listar_usuario.html', {'usuarios': usuarios})

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return redirect('listar_usuarios')  
        else:
            return render(request, 'listar_usuario.html', {'usuarios': self.get_queryset(), 'serializer': serializer})

class UsuarioUpdate(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        usuario = get_object_or_404(Usuario, pk=user_id)
        serializer = self.serializer_class(instance=usuario)
        return render(request, 'atualizar_usuario.html', {'serializer': serializer, 'usuario': usuario})
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        
        usuario = get_object_or_404(Usuario, pk=user_id)
        serializer = UsuarioUpdateSerializer(instance=usuario, data=request.data, partial=True)

         
        if serializer.is_valid():
            serializer.save()
            return redirect('listar') 
        return render(request, 'atualizar_usuario.html', {'serializer': serializer, 'usuario': usuario})
    
class DeletarUsuario(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        usuario = get_object_or_404(Usuario, pk=user_id)
        serializer = self.serializer_class(instance=usuario)
        return render(request, 'atualizar_usuario.html', {'serializer': serializer, 'usuario': usuario})
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        usuario = get_object_or_404(Usuario, pk=user_id)
        usuario.delete()
        return redirect('listar')

        
    
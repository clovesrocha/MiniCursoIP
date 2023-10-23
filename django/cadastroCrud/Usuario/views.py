from django.shortcuts import render, redirect, get_object_or_404  
from .models import Usuario  
from django.urls import reverse  
from django.core import serializers 
from .serializers import UsuarioSerializer,UsuarioUpdateSerializer 
from rest_framework.renderers import TemplateHTMLRenderer 
from rest_framework.response import Response 
from rest_framework import status, generics  

class CadastrarUsuario(generics.CreateAPIView):
    serializer_class = UsuarioSerializer
    def get(self, request, *args, **kwargs):
       
        serializer = self.serializer_class()
       
        return render(request, 'cadastrousuario.html', {'serializer': serializer})

    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
           
            serializer.save()
            
            return redirect('cadastro')

class ListarUsuario(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        
        usuarios = self.get_queryset()

        return render(request,'listarusuario.html', {'usuarios':usuarios})
    
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return redirect('listar')
    

class UpdateUsuario(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        usuario = get_object_or_404(Usuario, pk=user_id)
        serializer = self.serializer_class(instance=usuario)
        return render(request, 'atualizarusuario.html', {'serializer': serializer, 'usuario': usuario})
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        
        usuario = get_object_or_404(Usuario, pk=user_id)
        serializer = UsuarioUpdateSerializer(instance=usuario, data=request.data, partial=True)

         
        if serializer.is_valid():
            serializer.save()
            return redirect('listar') 
        return render(request, 'atualizarusuario.html', {'serializer': serializer, 'usuario': usuario})
    

class DeleteUsuario(generics.DestroyAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


    def get(self, request, *args, **kwargs):

        user_id = kwargs.get('pk')
        usuario = get_object_or_404(Usuario,pk=user_id)
        serializer = self.serializer_class(instance=usuario)
    
        return render(request, 'listarusuario.html',{'serializer':serializer,'usuario':usuario})
    
    def post(self, request, *args, **kwargs):

        user_id = kwargs.get('pk')
        usuario = get_object_or_404(Usuario,pk=user_id)

        usuario.delete()
        return redirect('listar')

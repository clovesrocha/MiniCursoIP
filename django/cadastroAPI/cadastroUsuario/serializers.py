from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):


    class Meta:

        model = Usuario
        fields ='__all__'


class UsuarioUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields= ('nome','sobrenome','idade','foto')

    nome = serializers.CharField(required=False) 
    sobrenome = serializers.CharField(required=False)
    idade = serializers.IntegerField(required=False)     
    foto = serializers.ImageField(required=False)       
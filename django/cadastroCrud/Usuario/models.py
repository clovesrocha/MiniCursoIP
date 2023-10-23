from django.db import models

class Usuario(models.Model):

    class Meta:

        db_table ='usuario'


    nome = models.CharField(max_length=100)    
    sobrenome = models.CharField(max_length=100)    
    idade = models.IntegerField(default=0)    
    foto = models.ImageField(upload_to='foto de perfil')


    def __str__(self):

        return self.nome    
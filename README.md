# Energeasy

Energeasy é um projeto desenvolvido por Helton dos Santos França, com contribuições de Vinícius Marques Ribeiro, que tem como objetivo conscientizar os usuários sobre diferentes conceitos de energia, incluindo elétrica, nuclear e solar. Além disso, o projeto visa desmistificar informações errôneas sobre energia, permitir o cadastro de dispositivos e realizar cálculos de economia de energia.

## Instalação

Para instalar o Energeasy, siga estas etapas:

1. Clone este repositório.
2. Certifique-se de ter o Python e o Django instalados.
3. Execute o comando `pip install -r requirements.txt` para instalar as dependências.

## Uso

Após a instalação, siga estas etapas para utilizar o Energeasy:

1. Execute o servidor Django localmente.
2. Acesse o aplicativo através do navegador da web.
3. Cadastre os dispositivos e explore os recursos disponíveis para aprender sobre diferentes formas de energia e calcular a economia de energia.

## Exemplo de Código

Aqui está um exemplo de código utilizado no projeto:

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.urls import reverse
from django.core import serializers
from .serializers import UsuarioSerializer, UsuarioupdateSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status, generics
from django.views.decorators.csrf import csrf_exempt

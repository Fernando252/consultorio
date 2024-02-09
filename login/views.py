from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from django.db.models import Count
from .models import Abogado, Clientes
from .models import Casos

def ver_casos(request):
    casos_por_abogado = Abogado.objects.annotate(num_casos=Count('casos'))
    contenido = {
        'casos_por_abogado': casos_por_abogado
    }
    template = "ver_casos.html"
    return render(request, template, contenido)



def casos_abogado(request,codigo_abogado):
    abogado = Abogado.objects.get(pk=codigo_abogado)
    casos_abogado = Casos.objects.filter(abogado=abogado)
    contenido = {
        'casos_abogado' : casos_abogado, 
        'abogado' : abogado,

    }
    template = "caso.html"
    return render(request, template, contenido)



def ver_abogados(request,):
    abogados =Abogado.objects.all()
    contenido = {
        'abogados': abogados
    }
    template = "abogados.html"
    return render(request, template, contenido)\
    

def ver_abogado(request,codigo_abogado):
    abogados = Abogado.objects.get(pk = codigo_abogado)
    contenido = {
        'abogados' : abogados 
    }
    template = "abogado.html"
    return render(request, template, contenido)



def ver_clientes(request,):
    clientes =Clientes.objects.all()
    contenido = {
        'clientes': clientes
    }
    template = "clientes.html"
    return render(request, template, contenido)


def ver_cliente(request,codigo_cliente):
    cliente = Clientes.objects.get(pk = codigo_cliente)
    contenido = {
        'cliente' : cliente 
    }
    template = "cliente.html"
    return render(request, template, contenido)

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

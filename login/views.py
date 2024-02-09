from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from .models import Abogado

def ver_abogados(request,):
    abogados =Abogado.objects.all()
    contenido = {
        'abogados': abogados
    }
    template = "abogados.html"
    return render(request, template, contenido)


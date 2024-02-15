"""consultorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login.views import registrar_cita, index,ver_casos,casos_abogado,registro_abogado, registro_cliente, login_cliente, subir_documento




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_cliente, name='inicio'),
    path('login_cliente/', login_cliente, name='login_cliente'),
    
    path('index/', index, name='index'),

    path('registrar_cita/', registrar_cita, name='registrar_cita'),

    path('registro_cliente/', registro_cliente, name='registro_cliente'),
    path('registro_abogado/', registro_abogado, name='registro_abogado'),

     path('subir_documento/', subir_documento, name='subir_documento'),

    path('ver_casos/', ver_casos),
    path('caso/<int:codigo_abogado>/', casos_abogado, name="detalle_casos"),



]
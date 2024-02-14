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
from login.views import registrar_cita, ver_abogados, ver_clientes,ver_abogado,ver_cliente, index,ver_casos,casos_abogado,citas,citas_clientes,registro_abogado, registro_cliente, login_cliente




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_cliente, name='inicio'),
    path('login_cliente/', login_cliente, name='login_cliente'),
    
    path('index/', index, name='index'),

    path('registrar_cita/', registrar_cita, name='registrar_cita'),

    path('registro_cliente/', registro_cliente, name='registro_cliente'),
    path('registro_abogado/', registro_abogado, name='registro_abogado'),
    
 
    





    path('abogados/', ver_abogados),
    path('abogado/<int:codigo_abogado>/', ver_abogado, name="detalle_abogados"),

    path('clientes/', ver_clientes),
    path('cliente/<int:codigo_cliente>/', ver_cliente, name="detalle_cliente"),

    path('ver_casos/', ver_casos),
    path('caso/<int:codigo_abogado>/', casos_abogado, name="detalle_casos"),

    path('citas/', citas),
    path('cita_cliente/<int:codigo_cliente>/', citas_clientes, name="detalle_citas"),


]
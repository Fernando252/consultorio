from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.db.models import Count
from .models import Abogado, Clientes, Cita, Casos
from .models import Clientes, Cita
from django.contrib.auth import authenticate, login
from django.contrib import messages


def registro_abogado(request):
    ESPECIALIDAD_CHOICES = Abogado.ESPECIALIDAD_CHOICES
    if request.method == 'POST':
        cedula = request.POST['cedula']
        nombrea = request.POST['nombrea']
        apellido = request.POST['apellido']
        celular = request.POST['celular']
        correo = request.POST['correo']
        tipos_especialidad = request.POST['tipos_especialidad']
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']
        
        contraseña_cifrada = make_password(contraseña)
        # Crear una instancia de Abogado y guardarla en la base de datos
        abogado = Abogado.objects.create(
            cedula=cedula,
            nombrea=nombrea,
            apellido=apellido,
            celular=celular,
            correo=correo,
            tipos_especialidad=tipos_especialidad,
            usuario=usuario,
            contraseña=contraseña_cifrada,
        )
        
        # Realizar cualquier otra acción o redirigir a una página específica
        return redirect('index.html')  # Cambia 'pagina_de_exito' con la URL deseada
    return render(request, 'registro_abogado.html', {'ESPECIALIDAD_CHOICES': ESPECIALIDAD_CHOICES})

# registo cliente
def registro_cliente(request):
    if request.method == 'POST':
        cedula = request.POST['cedula']
        nombrec = request.POST['nombrec']
        apellido = request.POST['apellido']
        direccion = request.POST['direccion']
        celular = request.POST['celular']
        correo = request.POST['correo']
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']

        # Cifra la contraseña antes de almacenarla
        contraseña_cifrada = make_password(contraseña)

        # Crea una instancia de Clientes y guárdala en la base de datos
        cliente = Clientes.objects.create(
            cedula=cedula,
            nombrec=nombrec,
            apellido=apellido,
            direccion=direccion,
            celular=celular,
            correo=correo,
            usuario=usuario,
            contraseña=contraseña_cifrada,
        )

        # Realiza cualquier otra acción o redirige a una página específica
        return redirect('index.html')  # Cambia 'index.html' con la URL deseada

    return render(request, 'registro_cliente.html')



def login_cliente(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']

        # Autentica al usuario
        user = authenticate(request, username=usuario, password=contraseña)

        if user is not None:
            # Inicia sesión si la autenticación es exitosa
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('index.html')  # Cambia 'index.html' con la URL deseada
        else:
            # Muestra un mensaje de error si la autenticación falla
            messages.error(request, 'Credenciales incorrectas.')

    return render(request, 'login_cliente.html')

#citas

def citas(request):
    citas_por_cliente = Clientes.objects.annotate(num_citas=Count('citas'))
    contenido = {
        'citas_por_cliente': citas_por_cliente
    }
    template = "citas.html"
    return render(request, template, contenido)


def citas_clientes(request,codigo_cliente):
    cliente = Clientes.objects.get(pk=codigo_cliente)
    citas_cliente = Cita.objects.filter(cliente=cliente)
    contenido = {
        'citas_cliente': citas_cliente,
        'cliente': cliente,
    }
    template = "cita_cliente.html"
    return render(request, template, contenido)


#casos

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

#abogados

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

#clientes

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
#index
def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.db.models import Count
from .models import Abogado, Casos, Clientes,Cita
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CitaForm, DocumentoForm, RegistroClienteForm, CitaForm1
from django.views.generic import ListView
from django.http import JsonResponse




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
        return redirect('index.html')  
    return render(request, 'registro_abogado.html', {'ESPECIALIDAD_CHOICES': ESPECIALIDAD_CHOICES})

# registo cliente
def registro_cliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.contraseña = make_password(form.cleaned_data['contraseña'])
            cliente.save()
            return redirect('login_cliente')  # Cambia 'login_cliente.html' con la URL correcta
    else:
        form = RegistroClienteForm()

    return render(request, 'registro_cliente.html', {'form': form})


def login_cliente(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']

        user = authenticate(request, username=usuario, password=contraseña)

        if user is not None:
          
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('index') 
        else:
           
            messages.error(request, 'Credenciales incorrectas.')

    return render(request, 'login_cliente.html')




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

def index(request):
    
    return render(request, 'index.html')


def registrar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            nueva_cita = form.save(commit=False)
            
            nueva_cita.save()
            return redirect('index')  # Cambia 'index' con el nombre de tu vista principal
    else:
        form = CitaForm()

    abogados = Abogado.objects.all()
    clientes = Clientes.objects.all()
    return render(request, 'registrar_cita.html', {'form': form, 'abogados': abogados, 'clientes': clientes})




def subir_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentoForm()

    return render(request, 'subir_documento.html', {'form': form})



    
    

def citas_t(request):
    citas = Cita.objects.all()
    contenido = {
        'citas' : citas
    }
    template = "cita_general.html"
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


def nueva_cita(request):
    contenido = {}
    if request.method == 'POST':
        contenido ['form'] = CitaForm(request.POST or None)
        if contenido ['form'].is_valid():
            contenido ['form'].save()
            return redirect('lista_citas')

    contenido ['instancia_cita'] = Cita()
    contenido ['form'] = CitaForm(
        request.POST or None,
        instance = contenido['instancia_cita']
    )
    template = 'registrar_cita1.html'
    return render(request, template, contenido)


def eliminar_cita(request, codigo_cita):
    cita = get_object_or_404(Cita, id=codigo_cita)

    if request.method == 'POST':
        cita.delete()
        return redirect('lista_citas')  
    return render(request, 'ver_cita.html', {'cita': cita})

def ver_cita(request, codigo_cita):
   c = {}
   c['cita'] =  get_object_or_404(Cita, pk=codigo_cita)
   return render(request, 'ver_cita.html', c)

def editar_cita(request, codigo_cita):
    cita = get_object_or_404(Cita, pk=codigo_cita)
    if request.method == 'POST':
        form = CitaForm1(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas') 
    else:
        form = CitaForm1(instance=cita)
    return render(request, 'editar_cita.html', {'form': form})


#calendario de citas

class CitaListView(ListView):
    model = Cita
    template_name = 'cita_list.html'
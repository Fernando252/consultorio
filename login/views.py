from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.forms import LoginForm

def login_view(request):
    templates='index.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Corrige aquí
                # Redirige a la página deseada después de iniciar sesión
                return redirect('login.html')
            else:
                # Muestra un mensaje de error si la autenticación falla
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
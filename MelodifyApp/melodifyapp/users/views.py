from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm  # Importamos el formulario
from .models import User  # Asegúrate de que el modelo User esté bien configurado
from .decorators import user_type_required

def inicio(request):
    return render(request, 'home.html')

# Vista de registro de usuario
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Crea el usuario
            return redirect('users:login')  # Redirigir al login después del registro
        else:
            return render(request, 'register.html', {'form': form, 'error': 'Hubo un error en el formulario.'})
    else:
        form = UserCreationForm()  # Crear una instancia vacía del formulario
    return render(request, 'register.html', {'form': form})

# Vista de inicio de sesión
def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('users:dashboard')  # Redirigir al dashboard
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas.'})

    return render(request, 'login.html')

# Vista del dashboard principal (solo para usuarios autenticados)
@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})

# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('users:login')  # Redirigir al login después de cerrar sesión

#--------------------------------------------------------------------------------------------------------------------------------

# Vista para el dashboard de músico (requiere login y tipo de usuario 'musico')
@login_required
@user_type_required('M')
def musico_dashboard(request):
    return render(request, 'musico_dashboard.html')

# Vista para el dashboard de oyente (requiere login y tipo de usuario 'oyente')
@login_required
@user_type_required('O')
def oyente_dashboard(request):
    return render(request, 'oyente_dashboard.html')

# Vista para el dashboard de productor (requiere login y tipo de usuario 'productor')
@login_required
@user_type_required('P')
def productor_dashboard(request):
    return render(request, 'productor_dashboard.html')

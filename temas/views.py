from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Tema
from .forms import TemaForm


def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('temas')
            except IntegrityError:
                return render(request, 'registro.html', {'form': UserCreationForm(), 'error': 'Este usuario ya existe'})
        else:
            return render(request, 'registro.html', {'form': UserCreationForm(), 'error': 'Las contraseñas no coinciden'})


@login_required
def temas(request):
    temas = Tema.objects.filter(usuario=request.user, fecha__isnull=True)
    return render(request, 'temas.html', {'temas': temas})


@login_required
def temas_completados(request):
    temas = Tema.objects.filter(usuario=request.user, fecha__isnull=False).order_by('-fecha')
    return render(request, 'temas.html', {'temas': temas})


@login_required
def crear_tema(request):
    if request.method == 'GET':
        return render(request, 'crear_tema.html', {'form': TemaForm()})
    else:
        form = TemaForm(request.POST)
        nuevo_tema = form.save(commit=False)
        nuevo_tema.usuario = request.user
        nuevo_tema.save()
        return redirect('temas')


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {'form': AuthenticationForm(), 'error': 'El usuario o la contraseña son incorrectos'})
        else:
            login(request, user)
            return redirect('temas')


@login_required
def detalle_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id, usuario=request.user)
    if request.method == 'GET':
        form = TemaForm(instance=tema)
        return render(request, 'detalle_tema.html', {'tema': tema, 'form': form})
    else:
        form = TemaForm(request.POST, instance=tema)
        form.save()
        return redirect('temas')


@login_required
def completar_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id, usuario=request.user)
    if request.method == 'POST':
        tema.fecha = timezone.now()
        tema.save()
        return redirect('temas')

@login_required
def eliminar_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id, usuario=request.user)
    if request.method == 'POST':
        tema.delete()
        return redirect('temas')

    return render(request, 'eliminar_tema.html', {'tema': tema})
from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')
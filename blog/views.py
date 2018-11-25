from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Post
from .models import Mantencion
from .models import Tarjeta
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'Mobike/index.html')

def login(request):
    return render(request, 'Mobike/Login.html')

def formulario(request):
    form = Post()

    if request.method == "POST":

        form.PrimerNombre = request.POST['PNombre']
        form.SegundoNombre = request.POST['SNombre']
        form.PrimerApellido = request.POST['PApellido']
        form.SegundoApellido = request.POST['SApellido']
        form.Run = request.POST['Run']
        form.dv = request.POST['BD']
        form.Telefono = request.POST['Telefono']
        form.Direccion = request.POST['Direccion']
        form.Comuna = request.POST['Comuna']
        form.Usuario = request.POST['Usuario']
        form.Contraseña = request.POST['Contraseña']
        form.Correo = request.POST['Correo']
        form.Trabajo = request.POST['UbiTrabajo']
        form.NumTajeta = request.POST['NumBanco']
        form.TipoBanco = request.POST['TipoBanco']
        form.save()

    return render(request, 'Mobike/Formulario.html')

def formuMantenimiento(request):
    form = Mantencion()

    if request.method ==  "POST":
        form.CodManten = request.POST['codigo']
        form.FechaMante = request.POST['Fecha']
        form.CodBici = request.POST['CodBici']
        form.Descripcion = request.POST['Descripcion']
        form.save()

    return render(request, 'Mobike/Mantencion.html')

def arrendarMapa(request):
    return render(request, 'Mobike/ArrendarMapa.html')

def arrendar(request):
    return render(request, 'Mobike/Arriendo.html')


def arrendarPosito(request):
    form = Tarjeta()

    if request.method == "POST":
        form.TarjetaPrepa = request.POST['codigo']
        form.save()
        return render(request, 'Mobike/TerminarArriendo.html')
        
    return render(request, 'Mobike/arriendopositivo.html')

def terminarArriendo (request):
    return render(request, 'Mobike/TerminarArriendo.html')

def graciasportodo (request):
    return render(request, 'Mobike/GraciasPorTodo.html')
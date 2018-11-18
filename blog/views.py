from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Post

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
        form.save()

    return render(request, 'Mobike/Formulario.html')
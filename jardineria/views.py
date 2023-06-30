from django.shortcuts import render
from .models import Usuario
# Create your views here.

def index(request):

    return render(request, "index.html")

def Nosotros(request):

    return render(request, "Nosotros.html")

def CreateCuenta(request):

    return render(request, "CreateCuenta.html")

def Catalogo(request):

    return render(request, "Catalogo.html")

def Login(request):

    return render(request, "Login.html")

def crud(request):
    usuario = Usuario.objects.all()
    context = {
        "usuario": usuario
    }
    return render(request, "pages/ListaUser.html", context)

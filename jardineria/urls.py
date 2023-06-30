from djangojardineria.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name = "index"),
    path("Nosotros.html", views.Nosotros, name = "Nosotros"),
    path("CreateCuenta.html", views.CreateCuenta, name = "CreateCuenta"),
    path("Catalogo.html", views.Catalogo, name = "Catalogo"),
    path("Login.html", views.Login, name = "Login"),
    path("ListaUser.html", views.crud, name = "crud"),
    path("index.html", views.index, name = "index"),
]

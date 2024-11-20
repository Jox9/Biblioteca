from django.shortcuts import render
from .models import Autor, Libro

def autores(request):
    autores = Autor.objects.all()
    data = {
        "autores" : autores
    }

    return render(request, "autores.html", data)

def libros(request):
    return render(request, "libros.html")
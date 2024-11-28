from django.shortcuts import render
from .models import Autor, Libro

# Autores
def autores(request): # lista de autores

    # post
    if request.method == "POST":
        nombre = request.POST.get("nombre-autor")
        nacionalidad = request.POST.get("nacionalidad-autor")
        edad = request.POST.get("edad-autor")

        autor = Autor(nombre=nombre, nacionalidad=nacionalidad, edad=edad)

        autor.save()

    # list data
    autores_dt = Autor.objects.all()
    data = {"autores": autores_dt}

    return render(request, "autores.html", data)


def crear_autor(request):
    return render(request, "crear_autor.html")

def editar_autor(request, id):
    autor_dt = Autor.objects.get(id=id)
    data = {"autor" : autor_dt}
    return render(request, "editar_autor.html", data)

# Libros
def libros(request):
    return render(request, "libros.html")

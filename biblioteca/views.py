from django.shortcuts import render
from .models import Autor, Libro

# Autores
def autores(request): # Pagina que lista autores

    # Recibe solicitudes para crear autores
    if request.method == "POST":
        nombre = request.POST.get("nombre-autor")
        nacionalidad = request.POST.get("nacionalidad-autor")
        edad = request.POST.get("edad-autor")

        autor = Autor(nombre=nombre, nacionalidad=nacionalidad, edad=edad)

        autor.save()

    # Datos, para listar autores
    autores_dt = Autor.objects.all()
    data = {"autores": autores_dt}

    return render(request, "autores.html", data)


def crear_autor(request): # Pagina para crear autores
    return render(request, "crear_autor.html")

def editar_autor(request, id): # Pagina para editar autores 
   
   # Datos para autocompletar formularios con el autor
   # correspondiente. Ejm: editar autor Marcos  id = 1 
    autor_dt = Autor.objects.get(id=id)
    data = {"autor" : autor_dt}
   
    return render(request, "editar_autor.html", data)

def eliminar_autor():
    pass


# Libros
def libros(request):
    return render(request, "libros.html")

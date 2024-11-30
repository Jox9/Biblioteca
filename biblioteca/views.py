from django.shortcuts import redirect, render
from .models import Autor, Libro

# Autores
def autores_page(request): # Pagina que lista autores

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


def crear_autor_page(request): # Pagina para crear autores
    return render(request, "crear_autor.html")

def editar_autor_page(request, id): # Pagina para editar autores 
   
   # Datos para autocompletar formularios con el autor
   # correspondiente. Ejm: editar autor Marcos  id = 1 
    autor_dt = Autor.objects.get(id=id)
    data = {"autor" : autor_dt}
   
    return render(request, "editar_autor.html", data)

def editar_autor(request):
    
    if request.method == "POST":
        id = request.POST.get("id-autor")
        nombre = request.POST.get("nombre-autor")
        nacionalidad = request.POST.get("nacionalidad-autor")
        edad = request.POST.get("edad-autor")

        autor = Autor.objects.get(id = id)

        autor.nombre = nombre
        autor.nacionalidad = nacionalidad
        autor.edad = edad

        autor.save()

    return redirect("autores_page")

def eliminar_autor(request, id):
    
    autor = Autor.objects.get(id = id)
    autor.delete()

    return redirect("autores_page")



# Libros
def libros_page(request):   # Lista

    libros_dt = Libro.objects.all()
    data = {"libros" : libros_dt}

    return render(request, "libros.html", data)


def añadir_libro_page(request): # Página para añadir
    pass   

def editar_libro_page(request, id): # Página para editar
    pass

def añadir_libro(request):  # Crear / Añadir
    pass

def editar_libro(request): # Editar
    pass

def eliminar_libro(request): # Eliminar
    pass
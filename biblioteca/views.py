from django.shortcuts import render

def autores(request):
    return render(request, "autores.html")

def libros(request):
    return render(request, "libros.html")
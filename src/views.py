from django.http import HttpResponse
from django.shortcuts import render


def pagina_inicial(request):
    return render(request, "index.html")

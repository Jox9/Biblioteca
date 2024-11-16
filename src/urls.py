# The `urlpatterns` list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/5.1/topics/http/urls/

from django.contrib import admin
from django.urls import path
from . import views
from biblioteca import views as biblioteca
from contactenos import views as contactenos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.pagina_inicial),
    path("autores", biblioteca.autores),
    path("libros", biblioteca.libros),
    path("contactenos", contactenos.contactenos)
]

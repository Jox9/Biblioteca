from django.contrib import admin
from django.urls import path
from . import views
from biblioteca import views as biblioteca
from contactenos import views as contactenos

urlpatterns = [
    path("admin/", admin.site.urls),
    # Pagina de Inicio
    path("", views.pagina_inicial, name="inicio"),
    path("contactenos", contactenos.contactenos),

    # Autores
    path("autores", biblioteca.autores_page, name="autores_page"),
    path("crear_autor", biblioteca.crear_autor_page, name="crear_autor_page"),
    path("editar_autor/<int:id>", biblioteca.editar_autor_page, name="editar_autor_page"),
    path("editar_autor", biblioteca.editar_autor, name="editar_autor"),
    path("eliminar_autor/<int:id>", biblioteca.eliminar_autor, name="eliminar_autor"),

    path("libros", biblioteca.libros),
]


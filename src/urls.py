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

    # Libros
    path("libros=", biblioteca.libros_page, name="libros_page"),
    path("añadir_libros=", biblioteca.añadir_libro_page, name="añadir_libro_page"),
    path("editar_libros=<int:id>", biblioteca.editar_libro_page, name="editar_libro_page"),
    path("añadir_libros", biblioteca.añadir_libro, name="añadir_libro"),
    path("editar_libros", biblioteca.editar_libro, name="editar_libro"),
    path("eliminar_libros/<int:id>", biblioteca.eliminar_libro, name="eliminar_libro"),
]


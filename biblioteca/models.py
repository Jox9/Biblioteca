from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre}"


class Libro(models.Model):
    codigo = models.CharField(max_length=20)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    genero = models.CharField(max_length=80)
    idioma = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()
    editorial = models.CharField(max_length=100)
    fk_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.titulo} - {self.fk_autor.nombre}"
        
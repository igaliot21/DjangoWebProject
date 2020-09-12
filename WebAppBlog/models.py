from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class categoria(models.Model):
    nombre = models.CharField(
        max_length=50, verbose_name="Categoria")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(
        auto_now_add=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre


class post(models.Model):
    titulo = models.CharField(
        max_length=50, verbose_name="Título del post")
    contenido = models.CharField(
        max_length=512, verbose_name="Contenido del post")
    imagen = models.ImageField(
        verbose_name="Imagen del servicio", upload_to='blog/img', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(categoria)
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(
        auto_now_add=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.titulo

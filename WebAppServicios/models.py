from django.db import models

# Create your models here.


class servicio(models.Model):
    titulo = models.CharField(
        max_length=50, verbose_name="Título del servicio")
    contenido = models.CharField(
        max_length=512, verbose_name="Contenido del servicio")
    imagen = models.ImageField(
        verbose_name="Imagen del servicio", upload_to='servicios/img')
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(
        auto_now_add=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.titulo

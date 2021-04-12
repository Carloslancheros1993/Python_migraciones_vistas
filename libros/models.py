from django.db import models

from autores.models import Autor
from editoriales.models import Editorial


class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    paginas = models.IntegerField()
    estatus_publicado = models.BooleanField()
    editorial = models.ForeignKey(
        Editorial,
        related_name='libros',
        on_delete=models.SET_NULL,
        null=True
    )
    autor = models.ForeignKey(
        Autor,
        related_name='autores',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nombre

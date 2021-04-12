from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre



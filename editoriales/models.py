from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
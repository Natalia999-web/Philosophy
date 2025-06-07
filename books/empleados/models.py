from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=50)
    foto_url = models.URLField()

    def __str__(self):
        return self.nombre

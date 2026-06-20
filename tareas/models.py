from django.db import models

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)     # lavar la ropa
    descripcion = models.TextField()              # lavar la ropa blanca y de color separadamente
    completado = models.BooleanField(default=False) # falso 

    def __str__(self):
        return self.titulo
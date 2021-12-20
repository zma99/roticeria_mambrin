from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=40, null=False, blank=False)
    imagen = models.ImageField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=False, blank=False)
    descripcion = models.TextField(max_length=100)
    precio = models.FloatField(null=False, blank=False)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
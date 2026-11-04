from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=1000, unique=True, verbose_name="Nombre de la Categoría")
    descripcion = models.TextField(verbose_name="Descripción")

#Mostrar nombre en panel de Administración
def __str__(self):
        return self.nombre
    
class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Lugar")
    descripcion = models.TextField(verbose_name="Descripción")
    ubicacion = models.CharField(max_length=200, verbose_name="Ubicación / Ciudad")
    anio_construccion = models.IntegerField(verbose_name="Año de Construcción", null=True, blank=True)
    
    # URL para simplificar el manejo de imagenes
    imagen = models.URLField(max_length=500, verbose_name="URL de la Imagen")
    
    #Clave Foranea (Muchos "LugarPatrimonial" pueden pertenecer a un "Categoria")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    
    #Mostrar nombre en panel de Administración
    def __str__(self):
        return self.nombre
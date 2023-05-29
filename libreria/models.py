import os
from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='libros/imagenes/', verbose_name='Imagen', null=True)
    pdf = models.FileField(upload_to='pdfs/', verbose_name='PDF', null=True)
    descripcion = models.TextField(verbose_name='Descripcion', null=True)
    
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        # Eliminar la imagen
        if self.imagen:
            path = self.imagen.path
            if os.path.exists(path):
                os.remove(path)

        # Eliminar el archivo PDF
        if self.pdf:
            path = self.pdf.path
            if os.path.exists(path):
                os.remove(path)

        super().delete(using=using, keep_parents=keep_parents)
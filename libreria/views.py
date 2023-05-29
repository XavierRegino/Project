from django.shortcuts import render, get_object_or_404
from .models import Libro
from .forms import LibroForm

from django.http import FileResponse
from libreria import models
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros':libros})

def crear(request):
    formulario = LibroForm(request.POST or None)
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request):
    return render(request, 'libros/editar.html')

def descargar_pdf(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    # Obtener la ruta del archivo PDF
    ruta_pdf = libro.pdf.path

    # Abrir el archivo PDF en modo binario
    with open(ruta_pdf, 'rb') as archivo_pdf:
        # Crear una respuesta de descarga del archivo
        response = FileResponse(archivo_pdf)
        # Establecer el encabezado para la descarga
        response['Content-Disposition'] = f'attachment; filename="{libro.pdf.name}"'
        return response
from django.shortcuts import render, get_object_or_404, redirect
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
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('/libreria/libros/')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('/libreria/libros/')
    return render(request, 'libros/editar.html', {'formulario': formulario})

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
    
def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('/libreria/libros/')
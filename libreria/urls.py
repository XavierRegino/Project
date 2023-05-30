from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static

app_name = 'libreria'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('libros/', views.libros, name='libros'),
    path('libros/crear/', views.crear, name='crear'),
    path('libros/editar/', views.editar, name='editar'),
    path('libros/<int:libro_id>/descargar-pdf/', views.descargar_pdf, name='descargar_pdf'),
    path('libros/eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>',views.editar, name='editar'),
]
# Configuración para servir archivos estáticos y de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path

from .views import (ActualizarLibros, CrearLibro, DetalleLibro, EliminarLibro,
                    ListarLibros)

urlpatterns = [
    path('listar/', ListarLibros.as_view(), name='leer'),
    path('detalle/<int:pk>/', DetalleLibro.as_view(), name='detalles'),
    path('crear/', CrearLibro.as_view(), name='crear'),
    path('actualizar/<int:pk>/', ActualizarLibros.as_view(), name='actualizar'),
    path('eliminar/<int:pk>/', EliminarLibro.as_view(), name='eliminar'),
]

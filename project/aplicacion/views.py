# Create your views here.
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Libros  # Asegúrate de importar tu modelo


class CrearLibro(SuccessMessageMixin, CreateView):
    model = Libros
    fields = "__all__"
    success_message = 'Libro Creado Correctamente!'
    template_name = 'crear.html'


class ListarLibros(ListView):
    model = Libros
    template_name = 'index.html'

class DetalleLibro(DetailView):
    model = Libros
    template_name = 'detalles.html'

class ActualizarLibros(SuccessMessageMixin, UpdateView):
    model = Libros
    fields = "__all__"
    success_message = 'Libro Actualizado Correctamente!'

    def get_success_url(self):
        return reverse('leer')

class EliminarLibro(SuccessMessageMixin, DeleteView):
    model = Libros

    def get_success_url(self):
        messages.success(self.request, 'Libro Eliminado Correctamente!')
        return reverse('leer')
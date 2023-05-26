from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from Usuario.models import Usuario
from .forms import FormularioUsuario

# Create your views here.
#Creacion CRUD para usuarios todo se realiza con vistas basadas en clases.

class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuario/listarUsuario.html'
    queryset = Usuario.objects.filter(usuario_activo=True)

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/crearUsuario.html'
    success_url = reverse_lazy('usuario:listar_usuario')


class EditarUsuario(UpdateView):
    model = Usuario
    template_name = "usuario/crearUsuario.html"
    form_class = FormularioUsuario
    success_url = reverse_lazy('usuario:listar_usuario')

class EliminarUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario:listar_usuario')



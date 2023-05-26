from django.urls import path
from django.contrib.auth.decorators import login_required
from Usuario.views import RegistrarUsuario, ListadoUsuario, EditarUsuario, EliminarUsuario

#Se pone el as_view() por ser una vista basada en clase.

urlpatterns = [
    path('listadoUsuarios/', login_required(ListadoUsuario.as_view()), name = 'listar_usuario'),
    path('registrarUsuario/', login_required(RegistrarUsuario.as_view()), name = 'registrar_usuario'),
    path('actualizarUsuario/<int:pk>/', login_required(EditarUsuario.as_view()), name = 'actualizar_usuario'),
    path('eliminarUsuario/<int:pk>/', login_required(EliminarUsuario.as_view()), name = 'eliminar_usuario'),
]
from django.urls import path
from Vivero import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import ViveroCreateView, ListarVivero, EditarVivero, EliminarVivero

from django.contrib.auth.decorators import permission_required

urlpatterns = [
    #path('', login_required(views.inicio), name="Inicio"),
    path('', login_required(ViveroCreateView.as_view()), name="registro_vivero"),
    path('listarVivero/',login_required(ListarVivero.as_view()), name="listar_vivero"),
    path('editarVivero/<int:pk>/', login_required(EditarVivero.as_view()), name='editar_vivero'),
    path('eliminarVivero/<int:pk>/', login_required(EliminarVivero.as_view()), name='eliminar_vivero'),
    path('descargarexcel', login_required(views.exportar_viveros_excel), name ="exportarexcel"),
    path('descargarpdf', login_required(views.exportar_viveros_pdf), name ="exportarpdf"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



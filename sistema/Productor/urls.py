from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.productor), name="Productor"),
    path('listarproductor', login_required(views.productor_list), name ="listarproductor"),
    path('editarproductor/<int:id>/', login_required(views.editar_productor), name ="editarproductor"),
    path('eliminarproductor/<int:id>/', login_required(views.eliminar_productor), name ="eliminarproductor")
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
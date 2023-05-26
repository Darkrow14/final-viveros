from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.labor), name = "Labor")
]
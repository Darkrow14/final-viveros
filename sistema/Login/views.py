from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from .forms import FormularioLogin

# Create your views here.
#def login(request):
#    return render(request, "login/login.html")

class Login(FormView):
    template_name = 'login/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('Inicio')

    #Utilizamos un decorador para un metodo para que no se almacene en cache la información correspondiente 
    #Y evitar las vulneraciones comunes en el desarrollo web
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("Entro a redireccionar la ruta.")
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

#Creacion del Logout o cerrar sesion
#Logout es una funcion que recibe la peticion y va a cerrar la sesion

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


#def menu_sesion(request):
#    return render(request, "login/barraSesion.html")

    
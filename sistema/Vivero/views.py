from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from .models import Vivero
from .forms import DepartamentoMunicipioVivero, FormularioVivero, FormularioMunicipio, FormularioDepartamento


# Create your views here.

#def vivero(request):
#    return render(request, "vivero/viveroFormulario.html")

class ViveroCreateView(CreateView):
    model = Vivero
    form_class = FormularioVivero
    template_name = 'vivero/viveroFormulario.html'
    #form_class = FormularioVivero
    #second_form_class = FormularioMunicipio
    #third_form_class = FormularioMunicipio
    #queryset = Vivero.objects.filter()
    success_url = reverse_lazy('vivero:listar_vivero')

    """
    def get_context_data(self, **kwargs):
        context = super(ViveroCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            vivero = form2.save(commit=False)
    """

    """
    def get_context_data(self, **kwargs):
        context = super(ViveroCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        if form.is_valid() and form2.is_valid and form3.is_valid:
            departamento = form2.save(commit=False)
            municipio = form3.save(commit=False)
            departamento.municipio = form3.save()
            departamento.vivero = form.save()
            departamento.save()
            return HttpResponseRedirect(self.get_success_url)
        else:
            return self.render_to_response(self.get_context_data(form = form, form2 = form2, form3 = form3))

    """



"""
    def form_valid(self, form):
        departamento = form['departamento'].save()
        municipio = form['municipio'].save(commit = False)
        vivero = form['vivero'].save(commit = False)
        municipio.departamento = departamento
        municipio.save()
        vivero.departamento = departamento
        vivero.save()
        return HttpResponseRedirect(reverse('success'))

class SuccessView(TemplateView):
    template_name = 'vivero/success.html'
"""


class ListarVivero(ListView):
    model = Vivero
    template_name = "vivero/tablaViveros.html"


class EditarVivero(UpdateView):
    model = Vivero
    template_name = "vivero/viveroFormulario.html"
    form_class = FormularioVivero
    success_url = reverse_lazy('vivero:listar_vivero')


class EliminarVivero(DeleteView):
    model = Vivero
    success_url = reverse_lazy('vivero:listar_vivero')







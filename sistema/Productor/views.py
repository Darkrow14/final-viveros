from django.shortcuts import render, redirect
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
#from django.shortcuts import render_to_response, get_object_or_404
from Productor.forms import FormularioProductor
from Productor.models import Productor
from django.views.generic.edit import CreateView
from django.contrib import messages

# Create your views here.
def productor(request):
    if request.method == 'POST':
        form = FormularioProductor(request.POST)
        if form.is_valid():
            #messages.success(request, 'Productor guardado')
            form.save()
        return redirect('Productor')
    else:
        form = FormularioProductor
    return render(request, 'productor/productores.html', {'form': form})


def productor_list(request):
    productor = Productor.objects.all()
    contexto = {'productores': productor}
    return render(request, 'productor/productoresTabla.html', contexto)


def editar_productor(request, id):
    productor = Productor.objects.get(id = id)

    if request.method == 'GET':
        form = FormularioProductor(instance=productor)
        contexto = { 'form': form }
    else:
        form = FormularioProductor(request.POST, instance = productor)
        contexto = { 'form': form }
        if form.is_valid():
            form.save()
            return redirect('listarproductor')
    return render(request, 'productor/productores.html', contexto)


def eliminar_productor(request, id):
    productor = Productor.objects.get(id = id)

    if request.method == 'POST':
        productor.delete()
        return redirect('listarproductor')
    return render(request, 'productor/confirmarEliminar.html', {'productor':productor})
    


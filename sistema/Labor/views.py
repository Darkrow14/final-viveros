from django.shortcuts import render

# Create your views here.
def labor(request):
    return render(request, "labor/labores.html")
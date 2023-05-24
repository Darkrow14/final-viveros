from django.shortcuts import render

#Create views
def inicio(request):
    return render(request, "vivero/index.html")
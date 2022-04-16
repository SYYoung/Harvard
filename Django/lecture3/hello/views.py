from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, Django!!!!")
    return render(request, "hello/index.html")
    
def brian(request):
    return HttpResponse("Hello, Sheena")
    
def david(request):
    return HttpResponse("What a great day, David.")
    
def greet(request, name):
    #return HttpResponse(f"Hello, {name}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

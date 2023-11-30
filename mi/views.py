from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohith(request):
    return render(request,'rohith.html')
def boomra(request):
    return HttpResponse('<h1>boom boom boomra</h1>')
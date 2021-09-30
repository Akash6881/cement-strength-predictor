from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')

def predict(request):

    cement = request.GET.get('cement', 'default')
    cement = float(cement)
    slag = request.GET.get('Slag')
    slag = float(slag)
    Flyash = request.GET.get('Flyash')
    Flyash = float(Flyash)
    Water = request.GET.get('Water')
    Water = float(Water)
    Superplasticizer = request.GET.get('Superplasticizer')
    Superplasticizer = float(Superplasticizer)
    ca = request.GET.get('ca')
    ca = float(ca)
    fa = request.GET.get('fa')
    fa = float(fa)
    return HttpResponse("hellp")
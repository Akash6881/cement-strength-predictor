from django.http import HttpResponse
from django.shortcuts import render


def predict(request):
    return HttpResponse("hellp")
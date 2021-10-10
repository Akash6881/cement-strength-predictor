from django.http import HttpResponse
from django.shortcuts import render
import joblib


scaler = joblib.load('./models/normal_scaler.pkl')
model = joblib.load('./models/rand_reg.pkl')


def index(request):

    return render(request, 'ml/index.html')

def predict(request):

    cement = request.GET.get('cement', 'default')
    cement = float(cement)
    slag = request.GET.get('Slag')
    slag = float(slag)
    age = request.GET.get('age')
    age = float(age)

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



    x_sclaed = scaler.transform([[cement, slag, Flyash, Water, Superplasticizer, ca, fa,age]])

    y = model.predict(x_sclaed)


    return HttpResponse(y)

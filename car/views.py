from django.shortcuts import render, render_to_response, HttpResponse
import datetime
from catalog.models import Brands

def index(request):
    return render_to_response('index.html')

def shapka(request):
    now_  = datetime.datetime.today()
    
    return render_to_response('shapka.html', locals())

def catalog(request):
    return render(request,'catalog.html',{"Марка: ": Brands.objects.all()})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fruits



def index(request):
    fruits = Fruits.objects.all()
    return render(request, 'fruits.html', {'fruits': fruits})


def add_fruit(request):
    if request.method == 'GET':
        return render(request, 'add_fruit.html')
    
    if request.method == 'POST':
        print(request.POST)
        return redirect('index')

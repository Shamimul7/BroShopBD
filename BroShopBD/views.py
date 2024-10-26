#Created by - Shamim
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def auth(request):
    return render(request, 'auth.html')
def contact(request):
    return render(request, 'home.html')
def search(request):
    return render(request, 'home.html')
def tracker(request):
    return render(request, 'home.html')
def prodView(request):
    return render(request, 'home.html')
def addCart(request):
    return render(request, 'home.html')
def checkout(request):
    return render(request, 'home.html')

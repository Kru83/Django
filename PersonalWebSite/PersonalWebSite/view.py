from django.shortcuts import render

def homepage(request):
    return render (request, 'index.html')

def weather(request):
    return render (request, 'weather.html')
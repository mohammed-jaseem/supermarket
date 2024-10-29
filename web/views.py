from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def features(request):
    return render(request, 'features.html')

def categories(request):
    return render(request, 'categories.html')

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')

def contact(request):
    return render(request, 'mysite/contact.html')

def portfolio(request):
    return render(request, 'mysite/portfolio.html')

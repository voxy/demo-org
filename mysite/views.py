from django.shortcuts import render
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')

def contact(request):
    return render(request, 'mysite/contact.html')

def portfolio(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.save(email=email,subject=subject,message=message)
    return render(request, 'mysite/portfolio.html')

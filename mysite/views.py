import json
from django.shortcuts import render, redirect
from .sso_request import get, url_for
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

def loginsso(request):
    if request.method == 'POST':
        euid = request.POST.get('euid')
        api_response = get(url_for('auth-token', euid=euid))
        __import__('pudb').set_trace()
        if api_response.status_code == 200:
            response_data = json.loads(api_response.content)
            return redirect(response_data['actions']['start'])
    return render(request, 'mysite/portfolio.html')

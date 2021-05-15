from django.shortcuts import render, redirect
from .models import users

# Create your views here.
def index(request):
    context= {
        'all_users': users.objects.all(),
    }
    return render(request, 'index.html', context)

def submit(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    age=request.POST['age']
    users.objects.create(first_name=first_name, last_name=last_name, email=email, age=age)
    return redirect('/')
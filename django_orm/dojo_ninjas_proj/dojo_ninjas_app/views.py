from django.shortcuts import render, redirect
from .models import dojos, ninjas

# Create your views here.

def index(request):
    context={
        'all_dojos': dojos.objects.all(),
        'all_ninjas': ninjas.objects.all()
    }
    return render(request,"index.html",context)

def addDojo(request):
    newname=request.POST['name']
    newcity=request.POST['city']
    newstate=request.POST['state']
    dojos.objects.create(name=newname, city=newcity, state=newstate)
    
    return redirect('/')

def addNinja(request):
    newfname=request.POST['first_name']
    newlname=request.POST['last_name']
    newdojo=request.POST['dojo']
    ninjas.objects.create(first_name=newfname, last_name=newlname, dojo=newdojo)
    
    return redirect('/')

def delete(request):
    pass
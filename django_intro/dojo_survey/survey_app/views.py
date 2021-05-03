from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def submit(request):
    request.session['result']={
        "name": request.POST["name"],
        "location": request.POST["location"],
        "language": request.POST["language"],
        "comments": request.POST["comments"]
    }
    return redirect('/result')

def result(request):
    result= request.session['result']
    return render(request,"result.html",result)
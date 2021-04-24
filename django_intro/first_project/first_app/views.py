from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # return HttpResponse("Placeholder to later display a list of all blogs")
    # return render(request, "index.html")
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}")

def destroy(request, number):
    return redirect('/')


from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.

def index(request):
    context = {
        "time_top": strftime("%b %d, %Y"),
        "time_bottom": strftime("%I:%M %p"),
    }
    return render(request,'index.html', context)
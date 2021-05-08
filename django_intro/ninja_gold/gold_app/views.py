from django.shortcuts import render, redirect
import random

gold_place = {
    "farm":(10,20),
    "cave":(5,10),
    "house":(2,5),
    "casino":(-50,50)
}
# Create your views here.
def index(request):
    if "gold" not in request.session or "activities" not in request.session:
        request.session["gold"] = 0
        request.session["activities"] =[]
    return render(request, 'index.html')

def submit(request):
    location= request.POST['location']
    gold_range=gold_place[location]
    gold_revenue=random.randint(gold_range[0],gold_range[1])
    request.session["gold"]+=gold_revenue
    message = f'You have earned {gold_revenue} from {location}! your current gold is {request.session["gold"]}'
    if location=="casino":
        if gold_revenue < 0:
            message=f'Ugh, you have lost {gold_revenue}, your current gold is {request.session["gold"]}, better luck next time!'
    
    request.session["activities"].append({"message": message})
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
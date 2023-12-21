from django.shortcuts import render,redirect
from .models import Food,Consume

def index(request):
    if request.method =="POST":
       # Get the name of the food from the Front-end
        food_consumed = request.POST['food_consumed']
       # Get the Food object on the BDD
        consume = Food.objects.get(name=food_consumed)
       # Get the user Login
        user = request.user
       # Make a link between user and consumed_food
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
    else:
        consumed_food = Consume.objects.filter(user=request.user)
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food': consumed_food, })


# Delete function

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')
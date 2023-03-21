from django.shortcuts import render
from . import models


def index(request):
    return render(request, "index.html")


def user(request):
    users = models.User.objects.all()
    return render(request, "user.html", context={"users": users})


def client(request):
    clients = models.Client.objects.all()
    return render(request, "client.html", context={"clients": clients})


def worker(request):
    workers = models.Worker.objects.all()
    return render(request, "worker.html", context={"workers": workers})


def food(request):
    food_pl = models.Food.objects.all()
    return render(request, "food.html", context={"food_pl": food_pl})


def ingredient(request):
    ingredients = models.Ingredient.objects.all()
    return render(request, "ingredient.html", context={"ingredients": ingredients})


def order(request):
    orders = models.Order.objects.all()
    return render(request, "order.html", context={"orders": orders})

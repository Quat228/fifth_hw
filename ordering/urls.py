from django.urls import path
from . import views


urlpatterns = [
    path("user", views.user, name="user"),
    path("client", views.client, name="client"),
    path("worker", views.worker, name="worker"),
    path("food", views.food, name="food"),
    path("ingredient", views.ingredient, name="ingredient"),
    path("order", views.order, name="order"),
    path("", views.index, name="index"),
]

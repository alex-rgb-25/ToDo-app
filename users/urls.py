from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
]
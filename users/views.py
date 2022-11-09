from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm, ToDoForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import ToDoList

def index(request):

    form = ToDoForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            txt= form.cleaned_data["todo"]
            td = ToDoList(user=request.user, text=txt)
            td.save()
            form = ToDoForm()
        return render(request, "users/index.html",{
            "form": form,
            "todos": ToDoList.objects.filter(user=request.user),
            "user": request.user
    })

    if request.user.is_authenticated:
        return render(request, "users/index.html",{
            "form": form,
            "todos": ToDoList.objects.filter(user=request.user),
            "user": request.user
        })
    else:
        return render(request, "users/index.html",{
            "form": form,
            "user": request.user
        })


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST) 

        if form.is_valid():
            form.save()   # saves in DB
            #directly login the user after registration:
            new_user = authenticate(username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect("/")
        return render(request,"users/register.html", {
                "form":form,
            })
    else:
        form=RegisterForm()
        return render(request, "users/register.html", {
            "form": form
        })


def delete_task(request, pk):
    task = ToDoList.objects.get(id=pk)  #get the todo that matches the id of the incoming request
    task.delete()
    return redirect("/")
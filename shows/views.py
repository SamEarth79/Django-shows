from django.shortcuts import render, redirect
from .models import Show
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def shows(request):
    if request.method == "POST":
        data = request.POST

        Show.objects.create(
            title=data["show_name"],
            fav=data["fav_character"],
            rating=float(data["show_rating"]),
        )

        print(Show.objects.all())
        return redirect("/")

    context = {"page": "Favourite shows", "data": Show.objects.all()}
    return render(request, "home.html", context)


def delete_show(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/")


def register(request):
    if request.method == "POST":
        data = request.POST

        if data["password"] != data["conf_password"]:
            return HttpResponse("Passwords do not match")

        user = User.objects.create(username=data["username"])

        user.set_password(data["password"])
        user.save()
        return redirect("/register/")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        data = request.POST

        user = User.objects.filter(username=data["username"])
        if not user.exists():
            return HttpResponse("Username invalid")

        user = authenticate(username=data["username"], password=data["password"])
        if user is None:
            return HttpResponse("Wrong credentials")

        login(request, user)
        return redirect("/")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")

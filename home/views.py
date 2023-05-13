from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    shows = [
        {"name": "Modern Family", "fav": "Phil Dunphy"},
        {"name": "B99", "fav": "Jake Peralta"},
    ]

    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "shows.html", context={"shows": shows})

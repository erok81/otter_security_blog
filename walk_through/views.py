from django.shortcuts import render
from django.http import HttpResponse

def walk_through(request):

    return render(request, "walkthrough.html")

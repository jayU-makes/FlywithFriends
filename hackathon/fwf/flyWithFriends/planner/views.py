from django.shortcuts import render
from .models import Plan, Places
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is the planner")

def planId(request, id = 0):
    if id == 0:
        index(request)
        return
    return HttpResponse("Your id is:"+str(id))

def edit(request, id = 0):
    if id == 0:
        index(request)
        return


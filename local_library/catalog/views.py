from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the home page!")

def about_view(request):
    return HttpResponse("This is the about page.")

# Create your views here.

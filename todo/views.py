from django.http import HttpResponse
from django.shortcuts import render

# We have to connect this view to the urls.py file to THIS app that will be checked in the urls.py of the whole project.
def index(request):
  return render(request,'todo/index.html')


def about(request):
  return render(request,'todo/about.html')
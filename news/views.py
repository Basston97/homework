from django.shortcuts import render
from django.http import HttpResponse

def get_new(request):
    return HttpResponse("Hello, world. We create ffirst view.")

# Create your views here.

from django.shortcuts import render
from django.shortcuts import HttpResponse


def show_news(request):
    
    return HttpResponse('Hello, Kitty!')

from django.shortcuts import render
from django.http import HttpResponse
from .models import Thread, Post
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')

def b(request):
    threads = Thread.objects.all()
    print(threads.first().post_set.first().id)
    #  
    context = {
        'name': 'Бред',
        'threads': threads
    }


    return render(request, 'board.html', context)

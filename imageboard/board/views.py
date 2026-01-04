from django.shortcuts import render
from django.http import HttpResponse
from .models import Thread, Post

threads = [
    {
        'id': 2,
        'title': 'Хопиума тред',
        'content': 'Сап, как думаете у меня получится запилить свой имиджборд?',
        'posted': '03-01-2026',
    },
    {
        'id': 1,
        'title': 'НГ тред',
        'content': 'Ну что аноны, уже есть новогоднее настроение?',
        'posted': '30-12-2025',
    },
    {
        'id': 0,
        'title': '0 GET',
        'content': '0 GET СОСАТЬ РАКИ',
        'posted': '29-12-2025',
    },
]


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
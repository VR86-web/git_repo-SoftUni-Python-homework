from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        'current_time': datetime.now(),
        'some_text': 'Hello my name is Vladislav, and i am learning Django Basics!',
        'users': [
            'Vladislav',
            'Milana',
            'Margarita',
            'Petar',
            'Tihomir',
        ]
     }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        'posts': [
            {
                'title': 'How to create Django project 1',
                'author': 'Vladislav R',
                'content': 'I still dont have a idea!',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create Django project 2',
                'author': '',
                'content': 'I still dont have a idea!',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create Django project 3',
                'author': 'Vladislav R',
                'content': '',
                'created_at': datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)

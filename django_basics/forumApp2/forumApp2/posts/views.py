from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        'current_time': datetime.now(),
        'some_text': 'This is some text!',
        'users': [
            'Pesho',
            'Gosho',
            'Maria',
            'Ivan',
            'Sasho',
        ]
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
            'posts': [
            {
                'title': 'My First Post',
                'content': 'This is the content of my first post.',
                'author': 'Pesho',
                'date_created': datetime.now(),
            },
            {
                'title': 'My Second Post',
                'content': 'This is the content of my second post.',
                'author': 'Pesho',
                'date_created': datetime.now(),
            },
            {
                'title': 'My Third Post',
                'content': 'This is the content of my third post.',
                'author': 'Pesho',
                'date_created': datetime.now(),
            },
            ],
    }

    return render(request, 'posts/dashboard.html', context)

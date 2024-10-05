from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        "current_time": datetime.now(),
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        'posts': [
            {
                'title': 'How to create Django projest 1?',
                'author': 'Vladislav',
                'content': 'I **dont** have a idea!',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create Django projest 2?',
                'author': 'Vladislav',
                'content': 'I dont have a idea!',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create Django projest 3?',
                'author': 'Vladislav',
                'content': 'I dont have a idea!',
                'created_at': datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)


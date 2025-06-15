from django.shortcuts import render

from regularExam.authors.models import Author


# Create your views here.


def index(request):
    has_author_profile = Author.objects.first()

    return render(request, 'common/index.html', {
        'has_author_profile': has_author_profile
    })


def dashboard(request):
    posts = Author.objects.filter()
    return render(request, 'common/dashboard.html')


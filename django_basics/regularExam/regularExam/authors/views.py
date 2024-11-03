from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from regularExam.authors.forms import AuthorCreateForm
from regularExam.authors.models import Author


# Create your views here.


class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')


def delete_author(request):
    return render(request, 'authors/delete-author.html')


def details_author(request):
    return render(request, 'authors/details-author.html')


def edit_author(request):
    return render(request, 'authors/edit-author.html')


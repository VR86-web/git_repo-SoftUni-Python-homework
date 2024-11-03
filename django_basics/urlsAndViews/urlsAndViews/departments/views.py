from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Hello User!')


def view_with_name(request, *args, **kwargs):
    return HttpResponse(f'Args: {args}, Kwargs: {kwargs}')


def view_with_int_pk(request, pk: int):
    return HttpResponse(f'Primary Key: {pk}')






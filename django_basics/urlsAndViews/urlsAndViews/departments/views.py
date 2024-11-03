from django.http import HttpResponse
from django.shortcuts import render

from urlsAndViews.departments.models import Department


# Create your views here.


def index(request):
    return HttpResponse('Hello User!')


def view_with_name(request, *args, **kwargs):
    return HttpResponse(f'Args: {args}, Kwargs: {kwargs}')


def view_with_int_pk(request, pk: int):
    return HttpResponse(f'Primary Key: {pk}')


def view_with_slug(request, slug):
    department = Department.objects.get(slug=slug)
    return HttpResponse(f"Department from slug: {department}")









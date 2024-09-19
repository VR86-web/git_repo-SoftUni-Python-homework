from django.http import HttpResponse
from django.shortcuts import render

from urlsAndViews.departments.models import Department


# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


def view_with_name(request, *args, **kwargs):
    return HttpResponse(f'Args: {args} -  Kwargs: {kwargs}')


def view_with_name_variable(request, variable):
    return HttpResponse(f'<h1>Variable: {variable}</h1>')


def view_with_int_pk(request, pk):
    return HttpResponse(f'<h1>Int pk with pk: {pk}</h1>')


def view_with_slug(request, slug):

    department = Department.objects.get(slug=slug)

    return HttpResponse(f'<h1>Department from slug: {department}</h1>')








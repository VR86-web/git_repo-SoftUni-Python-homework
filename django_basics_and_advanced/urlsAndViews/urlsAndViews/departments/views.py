from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from urlsAndViews.departments.models import Department


# Create your views here.


def index(request):
    return HttpResponse('Hello User!')


def view_with_name(request, variable):

    return render(request, 'departments/name_template.html', {'variable': variable})


def view_with_int_pk(request, pk: int):
    return HttpResponse(f'Primary Key: {pk}')


def view_with_slug(request, pk, slug):
    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f"Department from slug: {department}")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg/')


def redirect_to_view(request):
    return redirect('home')







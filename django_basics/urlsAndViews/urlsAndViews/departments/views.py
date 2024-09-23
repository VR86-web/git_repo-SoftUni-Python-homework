from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from urlsAndViews.departments.models import Department


# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


def view_with_name(request, *args, **kwargs):
    return HttpResponse(f'Args: {args} -  Kwargs: {kwargs}')


def view_with_name_variable(request, variable):
    #return HttpResponse(f'<h1>Variable: {variable}</h1>')
    return render(request, 'departments/name_template.html', {'variable': variable})


def view_with_int_pk(request, pk):
    return HttpResponse(f'<h1>Int pk with pk: {pk}</h1>')


def view_with_slug(request, slug):

    # Option 1 for 404
    # department = Department.objects.filter(slug=slug)

    # if not department:
    #    raise Http404

    # Option 2

    department = get_object_or_404(Department, slug=slug)

    return HttpResponse(f'<h1>Department from slug: {department}</h1>')


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')


def redirect_to_view(request):
    return redirect('home')






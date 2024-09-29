from django.shortcuts import render

# Create your views here.


def pet_add(request):
    return render(request, 'pets/pet-add-page.html')


def pets_details(request, username, pet_slug):
    return render(request, 'pets/pet-details-page.html')


def pets_edit(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')


def pets_delete(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')



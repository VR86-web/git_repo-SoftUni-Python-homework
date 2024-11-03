from django.shortcuts import render

# Create your views here.


def create_post(request):
    return render(request, 'posts/create-post.html')


def delete_post(request, post_id):
    return render(request, 'posts/delete-post.html')


def details_post(request, post_id):
    return render(request, 'posts/details-post.html')


def edit_post(request, post_id):
    return render(request, 'posts/edit-post.html')


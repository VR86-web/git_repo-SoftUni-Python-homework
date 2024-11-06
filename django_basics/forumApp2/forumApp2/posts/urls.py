from django.urls import path

from forumApp2.posts import views

urlpatterns = [
    path('', views.index, name='index'),
]


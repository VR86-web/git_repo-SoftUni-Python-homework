from django.urls import path

from forumApp.posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dash'),
]


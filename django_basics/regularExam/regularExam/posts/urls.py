from django.urls import path

from regularExam.posts import views

urlpatterns = {
    path('create/', views.create_post, name='create-post'),
    path('<post_id>/edit/ ', views.edit_post, name='edit-post'),
    path('<post_id>/delete/', views.delete_post, name='delete-post'),
    path('<post_id>/details/', views.details_post, name='details-post'),
}
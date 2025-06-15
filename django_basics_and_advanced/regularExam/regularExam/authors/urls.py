from django.urls import path

from regularExam.authors import views
from regularExam.authors.views import CreateAuthor

urlpatterns = {
    path('create/', CreateAuthor.as_view(), name='create-author'),
    path('edit/', views.edit_author, name='edit-author'),
    path('delete/', views.delete_author, name='delete-author'),
    path('details/', views.details_author, name='details-author'),
}

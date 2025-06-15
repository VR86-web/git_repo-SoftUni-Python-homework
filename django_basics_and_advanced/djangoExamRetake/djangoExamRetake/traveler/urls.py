from django.urls import path

from djangoExamRetake.traveler import views

urlpatterns = [
    path('create/', views.TravelerProfileCreateView.as_view(), name='create-traveler-view'),
]
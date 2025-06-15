from django.urls import path

from djangoExamRetake.alltrips import views

urlpatterns = [
    path('', views.AllTripsView.as_view(), name='all-trips'),
]
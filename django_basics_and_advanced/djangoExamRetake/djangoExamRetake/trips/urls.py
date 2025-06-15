from django.urls import path, include

from djangoExamRetake.trips import views

urlpatterns = [
    path('create', views.CreateTripView.as_view(), name='create-trip-view'),
    path('<trip_pk>/', include([
        path('details/', views.DetailView.as_view(), name='details-trip-view'),
    ]))
]
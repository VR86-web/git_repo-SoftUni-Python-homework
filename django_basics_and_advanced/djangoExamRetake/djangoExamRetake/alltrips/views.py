from django.shortcuts import render
from django.views.generic import ListView

from djangoExamRetake.trips.models import Trip


# Create your views here.


class AllTripsView(ListView):
    model = Trip
    template_name = 'trips/all-trips.html'
    context_object_name = 'trips'

    def get_queryset(self):
        return Trip.objects.all().order_by('-start_date')
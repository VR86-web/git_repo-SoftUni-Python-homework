
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from djangoExamRetake.trips.forms import TripCreateForm
from djangoExamRetake.trips.models import Trip
from utils import get_user_object


# Create your views here.


class CreateTripView(CreateView):
    model = Trip
    form_class = TripCreateForm
    template_name = 'trips/create-trip.html'
    success_url = reverse_lazy('all-trips')

    def form_valid(self, form):
        traveler = get_user_object()
        form.instance.traveler = traveler

        return super().form_valid(form)


class DetailsTripView(DetailView):
    template_name = 'trips/details-trip.html'
    model = Trip
    pk_url_kwarg = 'trip_pk'

    def get_object(self, queryset=None):
        return get_user_object()

    def get_queryset(self):
        return Trip.objects.filter(traveler=self.request.user)





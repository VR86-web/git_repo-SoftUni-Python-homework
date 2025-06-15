from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoExamRetake.traveler.forms import TravelerCreateForm
from djangoExamRetake.traveler.models import Traveler
from utils import get_user_object


# Create your views here.


class TravelerProfileCreateView(CreateView):
    model = Traveler
    form_class = TravelerCreateForm
    template_name = 'traveler/create-traveler.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_object()
        return super().form_valid(form)

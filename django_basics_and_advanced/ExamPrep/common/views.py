from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from ExamPrep.albums.models import Album
from ExamPrep.profiles.forms import ProfileCreateForm
from ExamPrep.utils import get_user_object


# Create your views here.


class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_user_object()

        if profile:
            return ['profiles/home-with-profile.html']
        else:
            return ['profiles/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


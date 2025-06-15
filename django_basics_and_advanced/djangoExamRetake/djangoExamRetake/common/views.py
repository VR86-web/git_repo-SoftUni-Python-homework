from django.views.generic import TemplateView

from utils import get_user_object


class IndexView(TemplateView):
    template_name = "common/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        traveler = get_user_object()

        context['traveler'] = traveler
        return context

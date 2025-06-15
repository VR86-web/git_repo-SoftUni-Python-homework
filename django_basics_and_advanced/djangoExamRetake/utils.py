from djangoExamRetake.traveler.models import Traveler


def get_user_object():
    return Traveler.objects.first()

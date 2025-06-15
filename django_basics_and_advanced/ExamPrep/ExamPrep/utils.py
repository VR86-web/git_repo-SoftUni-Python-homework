from ExamPrep.profiles.models import Profile


def get_user_object():
    return Profile.objects.first()
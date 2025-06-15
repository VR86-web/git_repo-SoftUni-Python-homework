from django.core.validators import MinLengthValidator
from django.db import models

from djangoExamRetake.traveler.validators import NicknameValidator


# Create your models here.


class Traveler(models.Model):

    nickname = models.CharField(
        unique=True,
        max_length=30,
        validators= [
            MinLengthValidator(3),
            NicknameValidator(),
        ],
        help_text="*Nicknames can contain only letters and digits."
    )

    email = models.EmailField(
        unique=True,
        max_length=30,
    )

    country = models.CharField(
        max_length=3,
        validators=[
            MinLengthValidator(3),
        ],
    )

    about_me = models.TextField(
        null=True,
        blank=True,
    )



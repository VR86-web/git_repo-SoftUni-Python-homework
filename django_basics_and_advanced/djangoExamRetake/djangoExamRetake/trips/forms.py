from django import forms

from djangoExamRetake.trips.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ('traveler', )
        widgets = {
            'summary': forms.TextInput(
                attrs={
                    'placeholder': "Share your exciting moments... ",
                }
            )
        }


class TripCreateForm(TripBaseForm):
    pass







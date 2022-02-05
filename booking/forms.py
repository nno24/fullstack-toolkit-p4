from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name',
            'email',
            'people',
            'date_time'
        ]

class RawBookingForm(forms.Form):
    date_time_raw = forms.DateTimeField(label='Select Date and time', widget=forms.DateTimeInput(attrs={
        'class': 'datepicker',
        'placeholder': 'Date and time for your booking'
    }))
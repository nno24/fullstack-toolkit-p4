from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(attrs={
        'class': 'forminput',
        'placeholder': 'Name'
    }))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={
        'class': 'forminput',
        'placeholder': 'Email'
    }))
    people = forms.IntegerField(label='Select how many', widget=forms.NumberInput(attrs={
        'class': 'forminput',
        'placeholder': 'How many are you ?'
    }))
    date = forms.DateField(label='Select Date', widget=forms.DateInput(attrs={
        'class': 'datepicker forminput',
        'placeholder': 'Date for your booking'
    }))
    time = forms.TimeField(label='Select Time', widget=forms.TimeInput(attrs={
        'class': 'timepicker forminput',
        'placeholder': 'Time for your booking'
    }))

    class Meta:
        model = Booking
        fields = [
            'name',
            'email',
            'people',
            'date',
            'time'
        ]

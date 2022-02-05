from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm, RawBookingForm


# Create your views here.


def get_home(request):
    return render(request, 'booking/home.html')
    
def back_home(request):
    return render(request, 'booking/home.html')

def get_booking(request):
    return render(request, 'booking/book.html')

def greeting(request):
    booking = Booking.objects.last()

    context = {
        'booking': booking
    }
    return render(request, 'booking/greeting.html', context)

""" def form_view(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookingForm()
        return redirect('greeting')
    
    context = {
        'form': form
    }
    return render(request, 'booking/form.html', context) """

def form_view(request):
    form = RawBookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RawBookingForm()
        return redirect('greeting')
    
    context = {
        'form': form
    }
    return render(request, 'booking/form.html', context)
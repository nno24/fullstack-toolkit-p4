from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm


# Create your views here.


def get_home(request):
    return render(request, 'booking/home.html')


def get_booking(request):
    if request.method == 'POST':
        print('the request is: ', request.POST.get('item_name'))
        return redirect('get_home')
    return render(request, 'booking/book.html')

def back_home(request):
    return render(request, 'booking/home.html')

 


from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Booking
from .forms import BookingForm


def push_email(date, time, email, name, people):
        send_mail(
        'Booking ' + date + ' at ' + time, #subject
        'Greetings ' + name + ' your booking was confirmed for ' + people + ' people.', #Message
        'staff@staff.staff', #from email
        [email] #to email
        )

# Create your views here.


def get_home(request):
    return render(request, 'booking/home.html')

def get_about(request):
    return render(request, 'booking/about.html')
    
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

def form_view(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        
        form_date = request.POST['date']
        form_time = request.POST['time']
        form_name = request.POST['name']
        form_people = request.POST['people']
        form_email = request.POST['email']

        #push_email(form_date, form_time, form_email, form_name, form_people)
        form = BookingForm()

        return redirect('greeting')
    
    context = {
        'form': form
    }

    return render(request, 'booking/form.html', context)

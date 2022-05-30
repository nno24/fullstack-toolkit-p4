from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import sessions
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
    """ A view to display the home page"""
    
    return render(request, 'booking/home.html')

def get_about(request):
    """A view to display the about page"""

    return render(request, 'booking/about.html')
    
def back_home(request):
    """A view to got back home"""

    return render(request, 'booking/home.html')

def get_booking(request):
    """"A view to display menu and booking button"""

    return render(request, 'booking/book.html')

def greeting(request):
    """A view to display successful booking"""

    booking = Booking.objects.get(id=request.session['user_id'])
    context = {
        'booking': booking,
    }
    return render(request, 'booking/greeting.html', context)

def form_view(request):
    """A view to render the input form and save new booking to db"""

    form = BookingForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
        except:
            return redirect('error')
# Get the session/user id 
        booking = Booking.objects.last()
        request.session['user_id']=booking.id

# Push_email(form_date, form_time, form_email, form_name, form_people)
        form = BookingForm()

        return redirect('greeting')
    
    context = {
        'form': form
    }

    return render(request, 'booking/form.html', context)

def manage(request):
    """A view to manage the booking"""

    if request.POST:
# Grab the changes in booking form and save to db
        this_booking = Booking.objects.get(id=request.session['user_id'])
        form = BookingForm(request.POST, instance=this_booking)
        if form.is_valid():
            try:
                form.save()
                return redirect('greeting')
            except:
                return redirect('error')
# If no post request, view what's already in the database
    else:
        try:  
            this_booking = Booking.objects.get(id=request.session['user_id'])
            form = BookingForm(instance=this_booking)
        except:
            return redirect('home')
    context = {
        'form': form,
    }

    return render(request, 'booking/manage.html', context)


def cancel(request):
    """A view to cancel booking"""

#Delete the booking
    try:
        booking = Booking.objects.get(id=request.session['user_id'])
        booking.delete()
    except:
        return redirect('error')

    context = {
        'booking': booking,
    }

    return render(request, 'booking/cancel.html', context)


def bookings(request):
    """A view to display the current users bookings"""
    try:
        booking = Booking.objects.get(id=request.session['user_id'])    
    except:
        return render(request, 'booking/nobookings.html')

    context = {
        'booking': booking,
    }        
    return render(request, 'booking/bookings.html', context)


def error(request):
    """A view to display error message"""

    context = {

    }

    return render(request, 'booking/error.html', context)
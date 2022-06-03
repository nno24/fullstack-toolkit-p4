from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import sessions, messages
from .models import Booking
from .forms import BookingForm
from datetime import datetime



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

def bookinglimit(request):
    """A view to display bookinglimit for anonymious users"""

    return render(request, 'booking/bookinglimit.html')

def greeting(request, booking_id):
    """A view to display successful booking"""

    if request.user.is_authenticated:
        booking = Booking.objects.get(id=booking_id, user=request.user.username)
    else:
        booking = Booking.objects.get(id=request.session['booking_id'])
    context = {
        'booking': booking,
    }
    return render(request, 'booking/greeting.html', context)

def form_view(request):
    """A view to render the input form and save new booking to db"""

    form = BookingForm(request.POST or None)
    if form.is_valid():
        try:
# Don't accept bookings in the past, so if today and earlier today            
            date = form.cleaned_data.get('date')
            time = form.cleaned_data.get('time')
            today_date = datetime.today().strftime('%Y-%m-%d')
            today_time = datetime.today().strftime('%H:%M:%S')
            if str(today_date) == str(date) and str(today_time) > str(time):
                messages.error(request, "Your booking time is invalid..")
                context = {
                    'form': form,
                }
                return render(request, 'booking/form.html', context)
            messages.success(request, "Booking confirmed")
            form.save()         
        except:
            return redirect('form')
# Get the booking id
        booking = Booking.objects.last()
        request.session['booking_id']=booking.id

# If user is authenticated, save the username to the booking.        
        if request.user.is_authenticated:
            booking.user = request.user.username
            booking.save()

        form = BookingForm()

        return redirect('greeting', booking_id=booking.id)
    
# Check if anonymious user already have a booking
    if not request.user.is_authenticated:
        try:
            last_booking = Booking.objects.get(id=request.session['booking_id'])
            return redirect('bookinglimit')
        except:
            pass

    context = {
        'form': form
    }

    return render(request, 'booking/form.html', context)

def manage(request, booking_id ):
    """A view to manage the booking"""

    if request.POST:
# Grab the booking depending if authenticated or not.
        if request.user.is_authenticated:
            this_booking = Booking.objects.get(id=booking_id, user=request.user.username)
        else:
            this_booking = Booking.objects.get(id=request.session['booking_id'])

        form = BookingForm(request.POST, instance=this_booking)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Booking saved")
                return redirect('greeting', booking_id=this_booking.id)
            except:
                return redirect('error')
# If no post request, view what's already in the database
    else:
        try:
            if request.user.is_authenticated:
                this_booking = Booking.objects.get(id=booking_id, user=request.user.username)
            else:  
                this_booking = Booking.objects.get(id=request.session['booking_id'])

            form = BookingForm(instance=this_booking)
        except:
            return redirect('home')
    context = {
        'form': form,
        'this_booking': this_booking,
    }

    return render(request, 'booking/manage.html', context)


def cancel(request, booking_id):
    """A view to cancel booking"""

#Delete the booking
    try:
        if request.user.is_authenticated:
            booking = Booking.objects.get(id=booking_id, user=request.user.username)
        else:
            booking = Booking.objects.get(id=request.session['booking_id'])
            
        booking.delete()
        messages.warning(request, "Your booking was cancelled..")
    except:
        return redirect('error')

    context = {
        'booking': booking,
    }

    return render(request, 'booking/cancel.html', context)


def bookings(request):
    """A view to display the current users bookings"""
    try:
# If the user is authenticated, grab all bookings related to the user
# If not, grab a single booking made by an anonymious user    
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user.username)
        else:
            bookings = Booking.objects.filter(id=request.session['booking_id'])
# Check if the queryset exist or not, if not show no bookings        
        if not bookings.exists():
            return render(request, 'booking/nobookings.html')
    except:
        return redirect('error')

    context = {
        'bookings': bookings,
    }        
    return render(request, 'booking/bookings.html', context)


def error(request):
    """A view to display error message"""

    context = {

    }

    return render(request, 'booking/error.html', context)
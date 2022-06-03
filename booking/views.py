from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import sessions, messages
from .models import Booking
from .forms import BookingForm
from datetime import datetime



# Functions ------------------------------------

def email_new_booking(date, time, email, name, people):
    """ Function to send emails for new bookings"""

    send_mail(
        'Booking pizzahaeven',
        'Greetings ' + name + ' your booking was confirmed for ' + people + ' people' + ' at time: ' + time + ' and date: ' + date,
        '',
        [email],
        fail_silently=False,
        )

def email_update_booking(date, time, email, name, people):
    """ Function to send emails for updated booking"""

    send_mail(
        'Booking pizzahaeven',
        'Greetings ' + name + ' your booking was updated for ' + people + ' people' + ' at time: ' + time + ' and date: ' + date,
        '',
        [email],
        fail_silently=False,
        )

def email_cancel_booking(date, time, email, name, people):
    """ Function to send emails for cancelled booking"""

    send_mail(
        'Booking pizzahaeven',
        'Greetings ' + name + ' your booking was CANCELLED for ' + people + ' people' + ' at time: ' + time + ' and date: ' + date,
        '',
        [email],
        fail_silently=False,
        )


# Cleanup routines for old bookings

def cleanup():
    """ A function to cleanup old bookings on the server"""

    bookings = Booking.objects.all()
    today_date = datetime.today().strftime('%Y-%m-%d')
    print("Checking if any old bookings..")
    for booking in bookings:
        if str(today_date) > str(booking.date):
            print("Deleting old booking: ", booking.id)
            booking.delete()

cleanup()

# Views ----------------------------------------

def home(request):
    """ A view to display the home page"""
    
    return render(request, 'booking/home.html')

def about(request):
    """A view to display the about page"""

    return render(request, 'booking/about.html')
    

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

            elif str(today_date) > str(date):
                messages.error(request, "Your booking date is invalid..")
                context = {
                    'form': form,
                }
                return render(request, 'booking/form.html', context)

            else:
                form.save()

# Push the email confirmation to the user
            em_date = form.cleaned_data.get("date")
            em_time = form.cleaned_data.get("time")
            em_email = form.cleaned_data.get("email")
            em_name = form.cleaned_data.get("name")
            em_people = form.cleaned_data.get("people")
            print(em_date, em_time, em_email, em_name, em_people)

            email_new_booking(str(em_date), str(em_time), str(em_email), str(em_name), str(em_people))
            messages.success(request, "Booking confirmed")
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
# Don't accept bookings in the past, so if today and earlier today            
                date = form.cleaned_data.get('date')
                time = form.cleaned_data.get('time')
                today_date = datetime.today().strftime('%Y-%m-%d')
                today_time = datetime.today().strftime('%H:%M:%S')
                if str(today_date) == str(date) and str(today_time) > str(time):
                    messages.error(request, "Your booking time is invalid..")
                    context = {
                        'form': form,
                        'booking_id': booking_id,
                    }
                    return redirect('manage', booking_id)

                elif str(today_date) > str(date):
                    messages.error(request, "Your booking date is invalid..")
                    context = {
                        'form': form,
                        'booking_id': booking_id,
                    }
                    return redirect('manage', booking_id)

                else:                
                    form.save()                
    # Push the email confirmation to the user
                em_date = form.cleaned_data.get("date")
                em_time = form.cleaned_data.get("time")
                em_email = form.cleaned_data.get("email")
                em_name = form.cleaned_data.get("name")
                em_people = form.cleaned_data.get("people")
                print(em_date, em_time, em_email, em_name, em_people)

                email_update_booking(str(em_date), str(em_time), str(em_email), str(em_name), str(em_people))

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
# Push the email confirmation to the user
        em_date = booking.date
        em_time = booking.time
        em_email = booking.email
        em_name = booking.name
        em_people = booking.people
        print(em_date, em_time, em_email, em_name, em_people)
        email_cancel_booking(str(em_date), str(em_time), str(em_email), str(em_name), str(em_people))

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
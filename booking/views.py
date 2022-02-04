from django.shortcuts import render

# Create your views here.


def get_home(request):
    return render(request, 'booking/home.html')


def get_booking(request):
    return render(request, 'booking/book.html')

def back_home(request):
    return render(request, 'booking/home.html')


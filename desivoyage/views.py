from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import TravelBooking
from django.http import HttpResponse



def home(request):
    return render(request, 'index.html')
def redirect_view(request):
    return render(request, 'rd.html')

def logout_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('redirect')  # Redirect to your home or dashboard page
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')
@csrf_protect   
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name= request.POST['name']
        email = request.POST['email']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exists Please try another username")
            return render(request, 'register.html')
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists Please try another email")
            return render(request, 'register.html')

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=name
        myuser.save()
        messages.success(request,"Your account has been successfully created")

        return redirect('login')




    return render(request, 'register.html')



def book_view(request):
    if request.method == 'POST':
        # Retrieve form data
        destination = request.POST.get('destination')
        departure_city = request.POST.get('departure-city')
        departure_date = request.POST.get('departure-date')
        return_date = request.POST.get('return-date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        travel_class = request.POST.get('travel-class')
        include_accommodation = request.POST.get('accommodation') == 'on'
        include_activities = request.POST.get('activities') == 'on'
        special_requirements = request.POST.get('special-requirements')

        # Create a new TravelBooking instance and save it to the database
        booking = TravelBooking(
            destination=destination,
            departure_city=departure_city,
            departure_date=departure_date,
            return_date=return_date,
            adults=adults,
            children=children,
            travel_class=travel_class,
            include_accommodation=include_accommodation,
            include_activities=include_activities,
            special_requirements=special_requirements,
        )
        booking.save()

        return HttpResponse("Booking submitted successfully. We will get back to you soon!")

    return render(request, 'bookform.html')

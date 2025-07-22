from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.dateparse import parse_date


@csrf_protect
@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if not user.is_deleted:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('home')  # Replace with your home URL name
            else:
                messages.error(request, "Your account has been deactivated.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


@csrf_protect
@never_cache
def welcome_view(request):
    return render(request, 'welcome.html')


User = get_user_model()

        # User registration details: 
        # Username: Ayoob
        # Email: ayoob@gmail.com
        # Password: ru_NW-r8epGeVQK
        # confirm Password: ru_NW-r8epGeVQK
        # dob: 2025-07-08
        # gender: Male
        # marital_status: Single
        # agree_to_terms: on

@csrf_protect
@never_cache
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        marital_status = request.POST.get('marital_status', '')
        terms = request.POST.get('terms', '')

        # Server-side validations
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('register')

        if len(password1) < 8:
            messages.error(
                request, "Password must be at least 8 characters long.")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        if terms != 'on':
            messages.error(
                request, "You must accept the terms and conditions.")
            return redirect('register')

        # Save user
        user = CustomUser.objects.create(
            username=username,
            email=email,
            password=make_password(password1),
            dob=parse_date(dob),
            gender=gender,
            marital_status=marital_status,
            agree_to_terms= True if terms == 'on' else False,
        )

        # print(f"""
        # User registration details: 
        # Username: {username}
        # Email: {email}
        # Password: {password1}
        # confirm Password: {password2}
        # dob: {dob}
        # gender: {gender}
        # marital_status: {marital_status}
        # agree_to_terms: {terms}
        # """)

        messages.success(request, "Registration successful. Please log in.")
        return redirect('login.html')

    return render(request, 'register.html')

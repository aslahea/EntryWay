from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


@csrf_protect
@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Server-side validation
        if not username or not password:
            messages.error(request, "Both fields are required.")
            return redirect('login')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('login')

        if len(password) < 8:
            messages.error(
                request, "Password must be at least 8 characters long.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(3600)  # Session expires in 1 hour
            messages.success(request, "Login successful.")
            return redirect('welcome')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


@csrf_protect
@never_cache
def welcome_view(request):
    return render(request, 'welcome.html')

User = get_user_model()

@csrf_protect
@never_cache
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # Server-side validations
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect('register.html')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('register.html')

        if len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('register.html')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register.html')

        # Save user
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password1)
        )

        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

    return render(request, 'register.html')

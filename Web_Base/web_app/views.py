from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterationForm
from .models import CustomUser


@csrf_protect
@never_cache
def register_view(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Succesfully. Please login.")
            return redirect('login')
        else:
            messages.error(request, "Error in Registration ")
    else:
        form = RegisterationForm()
    return render(request, 'register.html', {'form': form})


@csrf_protect
@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'home.html')


def user_list_view(request):
    users = CustomUser.objects.filter(is_deleted=False)
    return render(request, 'user_list.html', {'users': users})

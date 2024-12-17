from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from users.models import set_library_uesr_permission
from .forms import UserRegisterForm, UserLoginForm

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.save()

            set_library_uesr_permission(user)

            messages.success(
                request,
                "Registration successful. Redirecting to admin panel."
            )
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, "Registration failed. Please fix the errors below.")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@csrf_exempt
def user_login(request):

    if request.user.is_authenticated:
        return redirect('/dashboard/')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful. Redirecting to admin panel.")
            return redirect('/dashboard/')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

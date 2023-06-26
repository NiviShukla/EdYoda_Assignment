from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import MusicFile


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User registered successfully")
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(request, email=email, password=password)
            print("Authenticated user:", user)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def home(request):
    user = request.user
    allowed_files = MusicFile.objects.filter(
        access_type="public"
    ) | MusicFile.objects.filter(allowed_users=user)
    context = {"allowed_files": allowed_files}
    return render(request, "home.html", context)

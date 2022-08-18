import os

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CustomUserCreationForm


# Create your views here.
def dashboard(request):
    print(os.environ.get("EMAIL_HOST_USER"))
    print(os.environ.get("EMAIL_HOST_PASSWORD"))
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == 'GET':
        # pass the user creation form to html to collect user data
        return render(request, "users/register.html", {"form": CustomUserCreationForm})
    elif request.method == 'POST':
        # get the collect that we get from the form
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))

from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages


def homepage(request):
    return render(request=request,
                  template_name="main/home.html")


def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserRegisterForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})

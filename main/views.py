from django.shortcuts import render, redirect
from .forms import UserRegisterForm, PlaceOrderForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


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


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:homepage")


def order_request(request):
    if request.method == "POST":
        form = PlaceOrderForm(request.user, request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Order placed successfully.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful order. Invalid information.")
    form = PlaceOrderForm(request.user)
    return render(request=request,
                  template_name="main/order.html", context={"order_form": form})

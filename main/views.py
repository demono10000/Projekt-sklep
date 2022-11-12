import datetime

from django.shortcuts import render, redirect
from .forms import UserRegisterForm, SelectServiceForm, CompleteOrderForm, ChargeWalletForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import Order, Wallet


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
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to place an order.")
        return redirect("main:login")
    if request.method == "POST":
        form = CompleteOrderForm(request.user, request.POST)
        if form.is_valid():
            print('valid')
            if form.cleaned_data.get('quantity') <= 0:
                messages.error(request, "You must order at least 1 service.")
                return redirect("main:order")
            if not form.user_have_enough_money(Order.objects.get(user=request.user, paid=False).service, form.cleaned_data.get('quantity')):
                messages.error(request, "You don't have enough money to place this order.")
                return redirect("main:charge_wallet")
            form.save()
            return redirect("main:confirm")
        form = SelectServiceForm(request.user, request.POST)
        if not form.is_valid():
            messages.error(request, "Invalid information.")
            return redirect("main:order")
        if form.cleaned_data.get('service') is not None:
            order = Order.objects.filter(user=request.user, paid=False)
            if order.exists():
                order = order.first()
                order.service = form.cleaned_data.get('service')
                order.save()
            else:
                order = Order(user=request.user, service=form.cleaned_data.get('service'))
                order.save()
            form_new = CompleteOrderForm(request.user)
            form_new.fields['quantity'].initial = 1
            form_new.fields['quantity'].widget.attrs['min'] = 1
            return render(request=request,
                          template_name="main/order.html", context={"order_form": form_new,
                                                                    "description": form.cleaned_data.get(
                                                                        'service').description,
                                                                    "service": order.service})
        messages.error(request, "Unsuccessful order. Invalid information.")
    form = SelectServiceForm(request.user)
    return render(request=request,
                  template_name="main/order.html", context={"order_form": form})


def order_confirm(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to place an order.")
        return redirect("main:login")
    order = Order.objects.filter(user=request.user, paid=False)
    if not order.exists():
        messages.error(request, "You must select a service to place an order.")
        return redirect("main:order")
    order = order.first()
    if request.method == "POST":
        if order.service is None:
            messages.error(request, "You must select a service first.")
            return redirect("main:order")
        if order.url is None:
            messages.error(request, "You must enter a URL first.")
            return redirect("main:order")
        if order.quantity <= 0:
            messages.error(request, "You must order at least 1 service.")
            return redirect("main:order")
        wallet = Wallet.objects.get(user=request.user)
        if order.quantity * order.service.price > wallet.balance:
            messages.error(request, "You don't have enough money to place this order.")
            return redirect("main:charge_wallet")
        wallet.balance -= order.service.price * order.quantity
        wallet.save()
        order.paid = True
        order.paidDate = datetime.datetime.now()
        order.save()
        messages.success(request, "Order placed successfully.")
        return redirect("main:homepage")
    return render(request=request,
                  template_name="main/orderSummary.html", context={"orderData": order})


def charge_wallet_request(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to charge your wallet.")
        return redirect("main:login")
    if request.method == "POST":
        form = ChargeWalletForm(request.user, request.POST)
        if form.is_valid():
            if form.cleaned_data.get('amount') <= 0:
                messages.error(request, "You must charge more than 0$.")
                return redirect("main:charge_wallet")
            form.save()
            messages.success(request, "Wallet charged successfully.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful charge. Invalid information.")
    form = ChargeWalletForm(request.user)
    return render(request=request,
                  template_name="main/chargeWallet.html", context={"form": form})
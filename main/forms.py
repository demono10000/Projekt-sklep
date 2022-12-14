from datetime import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from main.models import Order, Service, Wallet


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        wallet = Wallet(user=user)
        wallet.save()
        return user


class CompleteOrderForm(forms.ModelForm):
    # service = forms.ModelChoiceField(queryset=Service.objects.all())
    quantity = forms.IntegerField()
    url = forms.URLField(max_length=200, required=True)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CompleteOrderForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = ['quantity', 'url']

    def save(self, commit=True):
        order = Order.objects.get(user=self.user, paid=False)
        # order.service = self.cleaned_data["service"]
        order.quantity = self.cleaned_data["quantity"]
        order.url = self.cleaned_data["url"]
        order.date = datetime.date(datetime.now())
        order.price = order.service.price * order.quantity
        # order.user_id = self.user.id
        if commit:
            order.save()
        return order

    def user_have_enough_money(self, service, quantity):
        wallet = Wallet.objects.get(user=self.user)
        return wallet.balance >= service.price * quantity


class SelectServiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all())

    class Meta:
        model = Order
        fields = ['service']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SelectServiceForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        order = super(SelectServiceForm, self).save(commit=False)
        order.service = self.cleaned_data["service"]
        if commit:
            order.save()
        return order


class ChargeWalletForm(forms.ModelForm):
    amount = forms.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        model = Wallet
        fields = ['amount']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChargeWalletForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        wallet = Wallet.objects.get(user=self.user)
        wallet.balance += self.cleaned_data["amount"]
        if commit:
            wallet.save()
        return wallet

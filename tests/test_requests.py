import datetime
from django.test import TestCase
from main.models import Service, Order, Wallet, OrderProxy
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.test import Client
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('main:login')
        self.logout_url = reverse('main:logout')
        self.register_url = reverse('main:register')
        self.home_url = reverse('main:homepage')
        self.order_url = reverse('main:order')
        self.confirm_url = reverse('main:confirm')
        self.charge_url = reverse('main:wallet')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.service = Service.objects.create(name='testservice', price=1.00, description='testdescription')
        self.order = Order.objects.create(user=self.user, service=self.service, quantity=1, url='testurl',
                                          paidDate=timezone.now(), price=1.00, completed=False, paid=False)
        self.wallet = Wallet.objects.create(user=self.user, balance=1000.00)

    def test_homepage_view_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_register_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/register.html')

    def test_register_view_POST(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': '123456',
            'password2': '123456'
        })
        self.assertEquals(response.status_code, 200)

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/login.html')

    def test_confirm_order_POST(self):
        balance = Wallet.objects.get(user=self.user).balance
        response = self.client.post(self.confirm_url, {
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Wallet.objects.get(user=self.user).balance, balance - self.order.price)
        self.assertEquals(Order.objects.get(user=self.user).paid, True)

    def test_charge_wallet_POST(self):
        balance = Wallet.objects.get(user=self.user).balance
        response = self.client.post(self.charge_url, {
            'amount': 100
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Wallet.objects.get(user=self.user).balance, balance + 100)

    def test_order_view_GET(self):
        response = self.client.get(self.order_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/order.html')

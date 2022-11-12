from django.urls import path
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('order/', views.order_request, name='order'),
    path('confirm/', views.order_confirm, name='confirm'),
    path('wallet/', views.charge_wallet_request, name='wallet'),
    path('orders/', views.check_order_status_request, name='ordersStatus'),
    path('orderInfo/<int:order_id>/', views.order_details_request, name='orderDetails'),
]
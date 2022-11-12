from django.contrib import admin

from main.models import Service, Order, Wallet, OrderProxy


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'sampleURL']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price', 'description']
    list_per_page = 25


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'service', 'quantity', 'url', 'paidDate', 'price', 'completed', 'paid']
    list_filter = ['user', 'service', 'quantity', 'url', 'paidDate', 'price', 'completed', 'paid']
    search_fields = ['user', 'service', 'quantity', 'url', 'paidDate', 'price', 'completed', 'paid']
    list_per_page = 25


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    list_filter = ['user', 'balance']
    search_fields = ['user', 'balance']
    list_per_page = 25


# paid orders, but not completed
@admin.register(OrderProxy)
class PendingOrdersAdmin(admin.ModelAdmin):
    # allow only for editing completed field
    list_display = ['id', 'user', 'service', 'quantity', 'url', 'paidDate', 'price', 'completed', 'paid']
    list_filter = ['user', 'service', 'quantity', 'url', 'paidDate', 'price', 'completed', 'paid']
    search_fields = ['user', 'service', 'quantity', 'url', 'paidDate', 'price', 'completed', 'paid']
    list_per_page = 25


    def get_queryset(self, request):
        return Order.objects.filter(paid=True, completed=False)


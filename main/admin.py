from django.contrib import admin

from main.models import Service, Order, Wallet


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price', 'description']
    list_per_page = 25


admin.site.register(Service, ServiceAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'service', 'quantity', 'url', 'date', 'price', 'completed']
    list_filter = ['user', 'service', 'quantity', 'url', 'date', 'price', 'completed']
    search_fields = ['user', 'service', 'quantity', 'url', 'date', 'price', 'completed']
    list_per_page = 25


admin.site.register(Order, OrderAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    list_filter = ['user', 'balance']
    search_fields = ['user', 'balance']
    list_per_page = 25


admin.site.register(Wallet, WalletAdmin)

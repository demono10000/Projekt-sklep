from django.contrib import admin

from main.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price', 'description']
    list_per_page = 25


admin.site.register(Service, ServiceAdmin)

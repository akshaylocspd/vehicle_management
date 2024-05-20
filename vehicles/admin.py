# admin.py

from django.contrib import admin
from .models import Vehicle, Chalan

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'owner', 'model', 'make', 'color', 'registered_on')
    search_fields = ('registration_number', 'owner__username', 'model', 'make', 'color')
    list_filter = ('make', 'color', 'registered_on')
    ordering = ('-registered_on',)

class ChalanAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'issued_on', 'amount', 'description')
    search_fields = ('vehicle__registration_number', 'amount', 'description')
    list_filter = ('issued_on', 'amount')
    ordering = ('-issued_on',)

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Chalan, ChalanAdmin)

from django.contrib import admin
from connection.models import Location, Contact


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'created_at', 'updated_at',)
    search_fields = ('location',)
    fields = ('location', 'lat', 'long',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'created_at', 'updated_at',)
    search_fields = ('phone',)
    fields = ('phone', 'email', 'telegram', 'instagram', 'facebook',)

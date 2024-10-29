from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=150)
    lat = models.DecimalField(max_digits=22, decimal_places=18, default=0)
    long = models.DecimalField(max_digits=22, decimal_places=18, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Contact(models.Model):
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

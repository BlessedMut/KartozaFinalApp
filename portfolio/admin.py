from django.contrib import admin

from portfolio.models import Profiles


@admin.register(Profiles)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "address", "phone", "lat", "lon")
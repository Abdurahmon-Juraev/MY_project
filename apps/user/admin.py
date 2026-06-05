from django.contrib import admin

from apps.user.models import User


@admin.register(User)
class Users(admin.ModelAdmin):
    list_display = ['name', 'phone_number']
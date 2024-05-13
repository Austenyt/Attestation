from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("id", "email", "name", "role",)
    list_filter = ()
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()

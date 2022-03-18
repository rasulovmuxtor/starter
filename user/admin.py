from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    pass

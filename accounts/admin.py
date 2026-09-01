from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin 

@admin.register(User)
class CustomAdminUser(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "first_name", "last_name", "role", "is_staff")
    ordering = ("email",)
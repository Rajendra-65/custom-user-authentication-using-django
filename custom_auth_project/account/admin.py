from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

class UserModelAdmin(UserAdmin):  # Class name should follow PascalCase
    model = User
    list_display = [
        "id",
        "email",
        "name",
        "is_active",
        "is_superuser",
        "is_staff",
        "is_customer",
        "is_seller",
    ]
    
    list_filter = ["is_superuser"]  # Fixed typo (list__filter → list_filter)
    
    fieldsets = (
        ("User Credentials", {"fields": ("email", "password")}),
        ("Personal Information", {"fields": ("name", "city")}),
        ("Permissions", {"fields": (
            "is_active",
            "is_staff",
            "is_superuser",
            "is_customer",
            "is_seller",
        )}),
    )

    search_fields = ["email"]
    ordering = ("email", "id")  # Tuples are preferred for ordering
    filter_horizontal = []

# Register the custom User model with the corrected admin class
admin.site.register(User, UserModelAdmin)

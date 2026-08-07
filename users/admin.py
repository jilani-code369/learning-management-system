from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA

from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(UA):
    list_display = ["id", "username", "first_name", "last_name", "email", "is_staff", "is_active", "is_superuser", "phone", "address", "dob", "gender"]
    list_editable = ["is_staff", "is_active", "is_superuser"]
    list_display_links = ["id", "username"]
    list_filter= ["is_active", "is_staff", "is_superuser"]
    list_per_page = 10
    search_fields = ["username", "first_name" ,"last_name"]
    
    
    fieldsets = (
          ( "Credentials", {"fields":("username", "password") } ),
          ("Infos", {"fields": ("first_name", "last_name", "email")}),
          ("Personal Infos", {"fields": ("phone", "address", "photo", "dob", "gender")}),
          ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
          ("Important Dates", {"fields":("date_joined", "last_login")}) 
      )
    
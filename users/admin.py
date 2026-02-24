from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User

from django.contrib import admin
from .models import ConsultantProfile

@admin.register(ConsultantProfile)
class ConsultantProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "license_number", "is_verified"]
    list_filter = ["is_verified"] 
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role", "is_verified", "is_staff")
    list_filter = ("role", "is_verified")
    search_fields = ("username", "email")
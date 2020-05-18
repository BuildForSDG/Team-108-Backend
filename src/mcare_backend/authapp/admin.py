from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)

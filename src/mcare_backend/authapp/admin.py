from django.contrib import admin
from .models import CustomUser, ExpertProfile


class CustomUserAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)



class ExpertProfileAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = ExpertProfile


admin.site.register(ExpertProfile, ExpertProfileAdmin)
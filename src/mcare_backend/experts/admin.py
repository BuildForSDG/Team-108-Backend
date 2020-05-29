from django.contrib import admin
from .models import ExpertProfile, ExpertClass, ClassModules


# Register your models here.
class ExpertProfileAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = ExpertProfile


admin.site.register(ExpertProfile, ExpertProfileAdmin)


class ExpertClassAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = ExpertClass


admin.site.register(ExpertClass, ExpertClassAdmin)


class ClassModulesAdmin(admin.ModelAdmin):
    '''Register the custom user model'''

    model = ClassModules


admin.site.register(ClassModules, ClassModulesAdmin)

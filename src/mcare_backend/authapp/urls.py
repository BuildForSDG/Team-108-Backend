from django.urls import path

from authapp.views import (
    customuser_registration_view
)

app_name = 'authapp'

urlpatterns = [
    path('register', customuser_registration_view, name='register'),
]
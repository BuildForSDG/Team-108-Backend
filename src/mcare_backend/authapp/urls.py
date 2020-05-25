from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from authapp.views import (
    customuser_registration_view,
    hello_world
)

app_name = 'authapp'

urlpatterns = [
    path('register', customuser_registration_view, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('helloworld', hello_world, name='helloworld')

]
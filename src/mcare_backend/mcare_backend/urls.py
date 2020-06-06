"""mcare_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from patients.urls import router as patient_router
from experts.urls import router as expert_router
from authapp.urls import router as auth_routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/authapp/', include('authapp.urls')),
    path('api/v1/user/', include(patient_router.urls)),
    path('api/v1/expert/', include(expert_router.urls)),
    path('api/v1/', include(auth_routers.urls)),
]

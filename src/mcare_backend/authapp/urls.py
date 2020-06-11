from django.urls import path

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authapp.views import (
    CustomUserViewSet,
    MyTokenObtainPairView
)

app_name = 'authapp'
router = routers.DefaultRouter()
router.register(r'register', CustomUserViewSet)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

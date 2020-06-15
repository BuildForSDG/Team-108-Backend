from django.urls import path

from rest_framework import routers

from rest_framework_simplejwt.views import TokenRefreshView

from authapp.views import (
    CustomUserViewSet,
    MyTokenObtainPairView,
    PatientUserViewSet,
    ExpertUserViewSet
)

app_name = 'authapp'
router = routers.DefaultRouter()
router.register(r'register', CustomUserViewSet)
router.register(r'patients', PatientUserViewSet)
router.register(r'experts', ExpertUserViewSet)


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

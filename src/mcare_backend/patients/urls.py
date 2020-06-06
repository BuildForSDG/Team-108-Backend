from django.urls import path, include

from rest_framework import routers

from .views import PatientProfileViewSet, PatientGroupViewSet, MessagesViewSet

router = routers.DefaultRouter()
router.register(r'profiles', PatientProfileViewSet)
router.register(r'groups', PatientGroupViewSet)
router.register(r'messages', MessagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

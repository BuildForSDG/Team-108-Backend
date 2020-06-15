from django.urls import path, include

from rest_framework import routers

from patients.views import (
    PatientGroupViewSet,
    MessagesViewSet
)

router = routers.DefaultRouter()
router.register(r'groups', PatientGroupViewSet)
router.register(r'messages', MessagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

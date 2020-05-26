from rest_framework import routers


from django.urls import path, include


from .views import PatientProfileViewSet


router = routers.DefaultRouter()
router.register(r'patients', PatientProfileViewSet)

# urlpatterns = [
#     path(r'patients/', include(router.urls)),
# ]
urlpatterns = router.urls
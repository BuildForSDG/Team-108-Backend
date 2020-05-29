from rest_framework import routers

from .views import PatientProfileViewSet, PatientGroupViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientProfileViewSet)
router.register(r'groups', PatientGroupViewSet)


# urlpatterns = [
#     path(r'patients/', include(router.urls)),
# ]
urlpatterns = router.urls

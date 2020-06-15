from rest_framework import routers


from .views import ExpertClassViewSet


router = routers.DefaultRouter()
router.register(r'classes', ExpertClassViewSet)

urlpatterns = router.urls

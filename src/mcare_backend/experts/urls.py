from rest_framework import routers


from .views import (
    ExpertClassViewSet,
    ExpertUserViewSet)


router = routers.DefaultRouter()
router.register(r'profiles', ExpertUserViewSet)
router.register(r'classes', ExpertClassViewSet)

urlpatterns = router.urls

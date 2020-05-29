from rest_framework import routers


from .views import ExpertProfileViewSet, ExpertClassViewSet


router = routers.DefaultRouter()
router.register(r'experts', ExpertProfileViewSet)
router.register(r'class', ExpertClassViewSet)


# urlpatterns = [
#     path(r'patients/', include(router.urls)),
# ]
urlpatterns = router.urls

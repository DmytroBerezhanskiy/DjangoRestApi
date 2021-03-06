from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet

router = DefaultRouter()

router.register(r"user", UserViewSet, basename="users")

urlpatterns = router.urls

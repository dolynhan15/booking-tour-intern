from django.urls import path, include
from rest_framework import routers

from .views.user import RegisterAPIView, UserViewSet, LoginAPIView, UserProfileViewSet

router = routers.SimpleRouter()
router.register("profiles", UserProfileViewSet, basename="profiles")
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),

]

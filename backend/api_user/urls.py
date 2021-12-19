from django.urls import path, include
from rest_framework import routers

from .views.user import RegisterAPIView, UserViewSet, LoginAPIView

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),

]

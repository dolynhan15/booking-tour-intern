from django.urls import path, include
from rest_framework import routers

from .views.review import ReviewViewSet

router = routers.DefaultRouter()
router.register("review", ReviewViewSet, basename="reviews")

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import routers, urlpatterns
from .views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register('', BookingTourAPIView, basename="booking")
urlpatterns = router.urls

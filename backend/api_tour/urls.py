from rest_framework import routers
from api_tour.views.tour import TourAPIView
from api_tour.views.tour_rating import TourRatingAPIView

app_name = "api_tour"
router = routers.DefaultRouter(trailing_slash=False)
router.register(r"rating", TourRatingAPIView, basename="rating")
router.register(r"", TourAPIView, basename="tour")
urlpatterns = router.urls

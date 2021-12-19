from api_booking_request.models import BookingRequest
from api_tour.models import Tour, TourRating


class TourRatingServices:
    @classmethod
    def create(cls, serializer, tour_id, rating, user):
        tour = Tour.objects.filter(pk=tour_id).first()
        return serializer.save(tour=tour, user=user,rating=rating)

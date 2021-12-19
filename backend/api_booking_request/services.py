from api_booking_request.models import BookingRequest
from api_tour.models import Tour


class BookingRequestServices:
    @classmethod
    def create(cls, serializer, tour_id, user):
        tour = Tour.objects.filter(pk=tour_id).first()
        if not Tour:
            return Exception(f"Tour is not found")
        return serializer.save(tour=tour, user=user)

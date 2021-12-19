from api_booking_request.models import BookingRequest
from api_category.models import Category
from api_tour.models import Tour
from api_place.models import Place


class TourServices:
    @classmethod
    def create(cls, data, category_id, list_place_id):
        print(category_id)
        category_obj = Category.objects.filter(pk=category_id).first()
        if not category_obj:
            return Exception(f"Category is not found")
        tour = Tour(**data, category=category_obj)
        place_obj = Place.objects.filter(pk__in=list_place_id)
        if not place_obj:
            return Exception(f"Place is not found")
        tour.save()
        tour.place.add(*place_obj)

        return tour

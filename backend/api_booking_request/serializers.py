from api_booking_request.models import BookingRequest
from rest_framework import serializers

from api_tour.serializers.tour import TourSerializer


class BookingRequestSerializer(serializers.ModelSerializer):
    tour = TourSerializer(many=False, read_only=True)

    class Meta:
        model = BookingRequest
        fields = "__all__"



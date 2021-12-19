from api_tour.models import Tour, TourRating
from rest_framework import serializers

from api_tour.serializers.tour import TourSerializer


class TourRatingSerializer(serializers.ModelSerializer):
    tour = TourSerializer(many=False, read_only=True)

    class Meta:
        model = TourRating
        fields = "__all__"

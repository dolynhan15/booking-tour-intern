from api_category.serializers import CategorySerializer
from api_place.serializers import PlaceSerializer
from api_tour.models import Tour
from rest_framework import serializers


class TourSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    place = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = "__all__"

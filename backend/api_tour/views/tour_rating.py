from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from api_tour.serializers.tour import *
from api_tour.models import TourRating
from api_tour.serializers.tour_rating import TourRatingSerializer
from api_tour.services.tour_rating import TourRatingServices
from api_user.models import User


class TourRatingAPIView(viewsets.ModelViewSet):
    queryset = TourRating.objects.all()
    serializer_class = TourRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                TourRatingServices.create(
                    serializer=serializer,
                    tour_id=request_data["tour_id"],
                    rating=request_data["rating"],
                    user=request.user,
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error_msg": str(e)})

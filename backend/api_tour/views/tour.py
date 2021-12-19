from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from api_tour.serializers.tour import *
from api_tour.models import Tour
from api_tour.services.tour import TourServices


class TourAPIView(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        category_id = request_data.pop('category_id')
        list_place_id = request_data.pop('list_place_id')
        serializer = self.get_serializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            try:
                tour = TourServices.create(
                    data=request_data,
                    category_id=category_id,
                    list_place_id=list_place_id,
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                # return Response(TourSerializer(tour).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error_msg": str(e)})

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from api_booking_request.serializers import *
from api_booking_request.services import BookingRequestServices
from api_user.models import User


class BookingTourAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                BookingRequestServices.create(
                    serializer=serializer,
                    tour_id=request.data["tour_id"],
                    user=request.user
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error_msg": str(e)})

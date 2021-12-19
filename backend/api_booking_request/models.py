from django.db import models
from api_base.models import BaseModel
from api_tour.models.tour import Tour
from api_user.models import User


class BookingRequest(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default=0, null=True)
    num_person = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = "api_booking_requests"



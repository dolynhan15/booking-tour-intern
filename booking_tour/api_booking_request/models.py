from django.db import models
from api_base.models import BaseModel
from api_tour.models.tour import Tour
from api_user.models import UserProfile


class BookingRequest(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default=0, null=True)
    num_person = models.IntegerField(default=1, null=True)
    discount = models.IntegerField(default=0, null=True)
    card_number = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = "api_booking_requests"



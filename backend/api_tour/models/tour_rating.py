from django.db import models
from api_base.models import BaseModel
from api_user.models import User
from api_tour.models.tour import Tour
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class TourRating(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

    class Meta:
        db_table = "api_tour_ratings"

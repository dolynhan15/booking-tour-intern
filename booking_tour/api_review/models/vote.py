from django.db import models
from api_base.models import BaseModel
from api_user.models import UserProfile
from api_review.models.review import Review


class Vote(BaseModel):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    status = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = "api_votes"


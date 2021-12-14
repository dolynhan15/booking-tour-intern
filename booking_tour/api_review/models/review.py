from django.db import models
from api_base.models import BaseModel
from api_review.models.vote import Vote
from api_user.models import UserProfile


class Review(BaseModel):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "api_reviews"

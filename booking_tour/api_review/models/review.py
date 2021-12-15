from django.db import models
from api_base.models import BaseModel
from api_tour.models import Tour
from api_user.models import User


class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "api_reviews"

    @property
    def num_vote(self):
        from api_review.models.vote import Vote
        return len(Vote.objects.filter(review=self.id))
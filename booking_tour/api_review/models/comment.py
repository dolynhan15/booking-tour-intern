from django.db import models
from api_base.models import BaseModel
from api_review.models.review import Review
from api_user.models import User


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "api_comments"


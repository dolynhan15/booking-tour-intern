from django.db import models
from api_base.models import BaseModel
from api_user.models import UserProfile


class Vote(BaseModel):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = "api_votes"

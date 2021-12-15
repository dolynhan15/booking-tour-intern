from django.db import models

from api_base.constant.user_constants import Genders
from api_base.models import BaseModel
from api_user.managers import UserProfileManager
from api_user.models import User


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    age = models.IntegerField(default=1, null=True)
    phone_number = models.CharField(max_length=10, null=True, )
    gender = models.IntegerField(
        choices=Genders.GENDERS, default=Genders.Select
    )
    photo = models.ImageField(
        max_length=255, blank=True, null=True
    )
    objects = UserProfileManager()

    class Meta:
        db_table = "api_user_profiles"

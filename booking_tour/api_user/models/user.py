from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from api_base.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(verbose_name="password", max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # staff is company admin
    admin = models.BooleanField(default=False)  # admin is super admin
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    class Meta:
        db_table = "api_users"

    def set_password(self, raw_password):
        self.password = make_password(password=raw_password, salt=settings.SECRET_KEY)
        self._password = raw_password

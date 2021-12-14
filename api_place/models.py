from django.db import models
from api_base.models import BaseModel
# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255)
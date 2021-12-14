from django.db import models
from api_base.models import BaseModel
# Create your models here.
class Review(BaseModel):
    content = models.CharField(max_length=255, null=True)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
from django.db import models
from api_base.models import BaseModel


# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "api_categories"

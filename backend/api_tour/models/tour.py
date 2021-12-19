from django.db import models
from api_base.models import BaseModel
from api_category.models import Category
from api_place.models import Place
from django.utils import timezone


class Tour(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    place = models.ManyToManyField(Place)
    name = models.CharField(max_length=255, null=True)
    start_date = models.DateField(auto_now=True, null=True)
    duration_morning = models.IntegerField(default=0, null=True)
    duration_evening = models.IntegerField(default=0, null=True)
    fare = models.IntegerField(default=0, null=True)
    discount = models.IntegerField(default=0, null=True)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "api_tours"
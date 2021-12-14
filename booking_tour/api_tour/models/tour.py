from django.db import models
from api_base.models import BaseModel
from api_category.models import Category
from api_place.models import Place
# Create your models here.

class Tour(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    duration_morning = models.IntegerField(default=0, null=True)
    duration_evening = models.IntegerField(default=0, null=True)
    fare = models.IntegerField(default=0, null=True)
    description = models.CharField(max_length=255, null=True)
    class Meta:
        db_table="api_tours"  
    
    
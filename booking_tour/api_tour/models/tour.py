from django.db import models
from api_base.models import BaseModel
from api_category.models import Category
from api_place.models import Place


class Tour(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    place = models.ManyToManyField(Place)
    name = models.CharField(max_length=255, null=True)
    duration_morning = models.IntegerField(default=0, null=True)
    duration_evening = models.IntegerField(default=0, null=True)
    fare = models.IntegerField(default=0, null=True)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "api_tours"

    @property
    def overall_rating(self):
        from api_tour.models import TourRating
        ratings = TourRating.objects.all().filter(tour=self.id)
        if len(ratings) > 0:
            return sum([x.rating for x in ratings]) / len(ratings)
        else:
            return 0

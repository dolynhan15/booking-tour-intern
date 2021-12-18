from django.contrib import admin
from .models import Comment, Review, Vote

admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Vote)
# Register your models here.

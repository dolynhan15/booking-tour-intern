from django.contrib import admin
from .models import User
from .models import UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
# Register your models here.

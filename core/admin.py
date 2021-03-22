from django.contrib import admin
from .models import User, Tracking, Habit, Profile



# Register your models here.



admin.site.register(User)
admin.site.register(Tracking)
admin.site.register(Habit)
admin.site.register(Profile)
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Habit(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField(max_length=10000, blank=True , null=True)
    goal = models.CharField(max_length=150)
    date = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.count}, {self.goal}, {self.date}'
    
    








from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_location = models.CharField(max_length=100)
    budget = models.FloatField()

    def __str__(self):
        return self.user.username

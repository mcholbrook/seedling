from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.

class Profile(models.Model):
  name = models.CharField(max_length=50)
  bio = models.TextField(max_length=200, blank=True)
  photo = models.CharField(max_length=200, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Profile for user: {self.name} at user_id {self.user_id}."
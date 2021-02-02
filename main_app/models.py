from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.

class Profile(models.Model):
  bio = models.TextField(max_length=200)
  photo = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Profile for user_id: {self.user_id}"
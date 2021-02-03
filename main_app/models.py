from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.
PRODUCE = (
  ('V', 'Vegetable'),
  ('FR', 'Fruit'),
  ('H', 'Herb'),
  ('FL', 'Flower')
)

class Profile(models.Model):
  bio = models.TextField(max_length=200, blank=True)
  photo = models.CharField(max_length=200, blank=True)
  zone = models.CharField('What gardening zone are you in?', max_length=15, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Profile for user: {self.name} at user_id {self.user_id}."

class Seed(models.Model):
  name = models.CharField(max_length=100)
  scientific_name = models.CharField('Scientific Name, if applicable', max_length=100, blank=True)
  kind = models.CharField(
    max_length=2,
    choices=PRODUCE,
    default=PRODUCE[0][0]
  )
  description = models.TextField(max_length=300, blank=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f"{self.name} seed, type {self.get_kind_display()}"
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

# FLOWER = 'Flower'
# HERB = 'Herb'

CARD_CHOICES = [
  ( 'FLOWER', 'Flower'),
  ('HERB', 'Herb'),
  ('ARUGULA', 'Arugula'),
]

# CARD_CHOICES = (
#   ('Flower', '../../static/images/Flower.png'),
#   ('Herb', '../../static/images/Herb.png')
# )

class Profile(models.Model):
  bio = models.TextField(max_length=200, blank=True)
  photo = models.CharField(max_length=200, blank=True)
  zone = models.CharField('What gardening zone are you in?', max_length=15, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  friends = models.ManyToManyField("self", symmetrical=False)

  def __str__(self):
    return f"Profile for user: {self.user.first_name} at user_id {self.user_id}, profile object {self.id}."

  # def get_absolute_url(self):
  #   return reverse('users_detail', kwargs={'user_id': self.user_id})

class Seed(models.Model):
  name = models.CharField(max_length=100)
  seed_source = models.CharField('Seed Source', max_length=100,  blank=True)
  kind = models.CharField(
    max_length=500,
    choices=CARD_CHOICES,
    default=CARD_CHOICES[0][0]
  )
  description = models.TextField(max_length=300, blank=True)
  users = models.ManyToManyField(User)

  def __str__(self):
    return f"{self.name} seed, type {self.get_kind_display()}"

class Note(models.Model):
  date = models.DateField()
  content = models.TextField(max_length=500)
  seed = models.ForeignKey(Seed, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.content} on {self.date}"

class Conversation(models.Model):
  participants = models.ManyToManyField(User)

class Message(models.Model):
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
  recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
  conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
  content = models.TextField('Your Message', max_length=500)
  date = models.DateField()


  
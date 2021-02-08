from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

# Create your models here.
PRODUCE = (
  ('V', 'Vegetable'),
  ('FR', 'Fruit'),
  ('H', 'Herb'),
  ('FL', 'Flower')
)

CARD_CHOICES = [
  ( 'flower', 'flower'),
  ('herb', 'herb'),
  ('arugula', 'arugula'),
  ('asparagus', 'asparagus'),
  ('basil', 'basil'),
  ('beans(green)', 'beans(green)'),
  ('beet', 'beet'),
  ('blueberries', 'blueberries'),
  ('bokchoy)', 'bokchoy'),
  ('broccoli', 'broccoli'),
  ('brussels', 'brussels'),
  ('cabbage(green)', 'cabbage(green)'),
  ('cabbage(red)', 'cabbage(red)'),
  ('calendula', 'calendula'),
  ('cantaloupe', 'cantaloupe'),
  ('carrots', 'carrots'),
  ('cauliflower', 'cauliflower'),
  ('chives', 'chives'),
  ('collards', 'collards'),
  ('corn', 'corn'),
  ('cucumber', 'cucumber'),
  ('daikon', 'daikon'),
  ('delicata', 'delicata'),
  ('dill', 'dill'),
  ('eggplant', 'eggplant'),
  ('eggplant(graffiti)', 'eggplant(graffiti'),
  ('fennel', 'fennel'),
  ('flower(other)', 'flower(other)'),
  ('fruit(other)', 'fruit(other)'),
  ('garlic', 'garlic'),
  ('jalapeno', 'jalapeno'),
  ('kale', 'kale'),
  ('lettuce', 'lettuce'),
  ('mint', 'mint'),
  ('onion', 'onion'),
  ('oregano', 'oregano'),
  ('parsley', 'parsley'),
  ('peas', 'peas'),
  ('peas(snow)', 'peas(snow)'),
  ('pepper(hot)', 'pepper(hot)'),
  ('pepper(bell)', 'pepper(bell)'),
  ('potato', 'potato'),
  ('pumpkin', 'pumpkin'),
  ('radish', 'radish'),
  ('raspberries', 'raspberries'),
  ('rhubarb', 'rhubarb'),
  ('sage', 'sage'),
  ('scallions', 'scallions'),
  ('spinach', 'spinach'),
  ('squash(acorn)', 'squash(acorn)'),
  ('squash(butternut)', 'squash(butternut'),
  ('squash(summer)', 'squash(summer)'),
  ('strawberries', 'strawberries'),
  ('tarragon', 'tarragon'),
  ('thyme', 'thyme'),
  ('tomato', 'tomato'),
  ('tomato(cherry)', 'tomato(cherry)'),
  ('tomato(heirloom)', 'tomato(heirloom)'),
  ('turnip', 'turnip'),
  ('veggie(other)', 'veggie(other)'),
  ('watermelon', 'watermelon'),
  ('yam', 'yam'),
]

class Profile(models.Model):
  bio = models.TextField(max_length=200, blank=True)
  photo = models.CharField(max_length=200, blank=True)
  zone = models.CharField('What gardening zone are you in?', max_length=15, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  friends = models.ManyToManyField("self", symmetrical=False, blank=True)

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
  date = models.DateField(default=datetime.now)
  content = models.TextField(max_length=500)
  seed = models.ForeignKey(Seed, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.content} on {self.date}"

  class Meta:
    ordering = ['-date']

class Conversation(models.Model):
  participants = models.ManyToManyField(User)

class Message(models.Model):
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
  recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient', blank=True)
  conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True)
  content = models.TextField('Your Message', max_length=500)
  date = models.DateField(default=datetime.now)
  seed = models.ForeignKey(Seed, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return f"{self.sender} and {self.recipient} on {self.date}"
  

class Garden(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Garden, id: {self.id}"

class Todo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField(default=datetime.now)
  garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
  content = models.CharField(max_length=200)

  def __str__(self):
    return f"Todo: {self.content}"
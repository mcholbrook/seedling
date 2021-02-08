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

# FLOWER = 'Flower'
# HERB = 'Herb'

CARD_CHOICES = [
  ( 'Flower', 'Flower'),
  ('Herb', 'Herb'),
  ('Arugula', 'Arugula'),
  ('Asparagus', 'Asparagus'),
  ('Basil', 'Basil'),
  ('Beet', 'Beet'),
  ('Broccoli', 'Broccoli'),
  ('Brussels', 'Brussels'),
  ('Cabbage(green)', 'Cabbage(green)'),
  ('Cabbage(red)', 'Cabbage(red)'),
  ('Calendula', 'Calendula'),
  ('Carrots', 'Carrots'),
  ('Cauliflower', 'Cauliflower'),
  ('Corn', 'Corn'),
  ('Cucumber', 'Cucumber'),
  ('Daikon', 'Daikon'),
  ('Dill', 'Dill'),
  ('Eggplant', 'Eggplant'),
  ('Fennel', 'Fennel'),
  ('Garlic', 'Garlic'),
  ('Kale', 'Kale'),
  ('Lettuce', 'Lettuce'),
  ('Mint', 'Mint'),
  ('Onion', 'Onion'),
  ('Oregano', 'Oregano'),
  ('Parsley', 'Parsley'),
  ('Peas', 'Peas'),
  ('Pepper(hot)', 'Pepper(hot)'),
  ('Pepper(bell)', 'Pepper(bell)'),
  ('Potato', 'Potato'),
  ('Pumpkin', 'Pumpkin'),
  ('Radish', 'Radish'),
  ('Spinach', 'Spinach'),
  ('Tarragon', 'Tarragon'),
  ('Thyme', 'Thyme'),
  ('Tomato', 'Tomato'),
  ('Tomato(cherry)', 'Tomato(cherry)'),
  ('Tomato(heirloom)', 'Tomato(heirloom)'),
  ('Beans(green)', 'Beans(green)'),
  ('Bokchoy)', 'Bokchoy'),
  ('Chives', 'Chives'),
  ('Collards', 'Collards'),
  ('Delicata', 'Delicata'),
  ('Eggplant(graffiti)', 'Eggplant(graffiti'),
  ('Jalapeno', 'Jalapeno'),
  ('Peas(snow)', 'Peas(snow)'),
  ('Rhubarb', 'Rhubarb'),
  ('Sage', 'Sage'),
  ('Scallions', 'Scallions'),
  ('Squash(acorn)', 'Squash(acorn)'),
  ('Squash(butternut)', 'Squash(butternut'),
  ('Squash(summer)', 'Squash(summer)'),
  ('Turnip', 'Turnip'),
  ('Yam', 'Yam'),
  ('Blueberries', 'Blueberries'),
  ('Cantaloupe', 'Cantaloupe'),
  ('Flower(other)', 'Flower(other)'),
  ('Fruit(other)', 'Fruit(other)'),
  ('Raspberries', 'Raspberries'),
  ('Strawberries', 'Strawberries'),
  ('Watermelon', 'Watermelon'),
  ('Veggie(other)', 'Veggie(other)')
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
  date = models.DateField(default=datetime.now)
  content = models.TextField(max_length=500)
  seed = models.ForeignKey(Seed, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.content} on {self.date}"

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
  
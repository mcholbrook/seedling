
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Seed, Note, Message, Conversation, Todo
from django.contrib.auth.forms import UserCreationForm

# class UserForm(ModelForm):
#     class Meta: 
#         model = User
#         fields = ['first_name', 'username', 'email', 'password']

class UserForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = User
    fields = ['username', 'first_name', 'email']


class SeedCreateForm(ModelForm):
  class Meta:
    model = Seed
    fields = ['name', 'seed_source', 'kind', 'description', 'maturity', 'spacing', 'grow_directions']

class NoteCreateForm(ModelForm):
  class Meta:
    model = Note
    fields = ['date', 'content']

class MessageCreateForm(ModelForm):
  class Meta:
    model = Message
    fields = ['recipient', 'content']

class ReplyForm(ModelForm):
  class Meta:
    model = Message
    fields = ['content']

class TodoForm(ModelForm):
  class Meta:
    model = Todo
    fields = ['content']

from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class UserForm(ModelForm):
#     class Meta: 
#         model = User
#         fields = ['first_name', 'username', 'email', 'password']

class UserForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = User
    fields = ['first_name', 'username', 'email']
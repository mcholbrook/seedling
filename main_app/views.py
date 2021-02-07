from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Profile, User, Seed, Note
from .forms import UserForm, SeedCreateForm, NoteCreateForm
from PIL import Image
# Create your views here.

def home(request):
  # chamomile = Image.open('.static/images/chamomile.png')
  return render(request, 'home.html')

def users_index(request):
  users = User.objects.all()
  print(users)
  return render(request, 'users/index.html', {'users': users})

def users_detail(request, userName_id):
  userWhoOwnsProfile = User.objects.get(id=userName_id)
  profile = Profile.objects.get(user=userName_id)
  return render(request, 'users/detail.html', { 'userAssociatedWithProfile': userWhoOwnsProfile, 'profile': profile })

def add_friend(request, profile_id, otheruser_id):
  friend = Profile.objects.get(id=profile_id)
  currentUser = Profile.objects.get(user_id=otheruser_id)
  print(f"You are adding this person {friend} to {currentUser}'s friend list")
  currentUser.friends.add(friend)
  return redirect('users_detail', userName_id=friend.user_id)

def delete_friend(request, profile_id, otheruser_id):
  friend = Profile.objects.get(id=profile_id)
  currentUser = Profile.objects.get(user_id=otheruser_id)
  # print(currentUser.friends.all())
  currentUser.friends.remove(profile_id)
  # print(currentUser.friends.all())
  currentUser.save()
  print(f'You have removed this friend: {friend}')
  return redirect('users_detail', userName_id=friend.user_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('create_profile')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProfileCreate(CreateView):
  model = Profile
  fields = ['bio', 'photo', 'zone']
  success_url = '/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['bio', 'photo', 'zone']

def seed_create(request):
  CARD_CHOICES = (
  ('Flower', 'Flower'),
  ('Herb', 'Herb')
  )
  print(Seed.kind)
  # kindlist = []
  # for choice in CARD_CHOICES:
  #   kindlist.append(choice[0])
  form = SeedCreateForm(request.POST)
  context = {'form': form}
  if form.is_valid():
    new_seed = form.save()
    print(new_seed.id)
    Seed.objects.get(id=new_seed.id).users.add(request.user)
    return redirect('/seeds/')
  return render(request, 'main_app/seed_form.html', context)


def seed_list(request):
  seeds = Seed.objects.all()
  return render(request, 'seeds/index.html', {'seeds': seeds})

def seeds_detail(request, seed_id):
  seed = Seed.objects.get(id=seed_id)
  note_form = NoteCreateForm()
  if User.objects.get(id=request.user.id).seed_set.filter(id=seed_id):
    print('User has this seed already')
    has_seed = True
  else:
    print('User does not have this seed')
    has_seed = False
  # does_user_have_seed = User.objects.get(id=request.user.id)
  return render(request, 'seeds/detail.html', {'seed': seed, 'note_form': note_form, 'has_seed': has_seed})

def add_note(request, seed_id):
  form = NoteCreateForm(request.POST)
  if form.is_valid():
    new_note = form.save(commit=False)
    print(new_note)
    new_note.seed_id = seed_id
    new_note.user_id = request.user.id
    new_note.save()
  return redirect('seeds_detail', seed_id=seed_id)

def save_seed(request, seed_id, user_id):
  Seed.objects.get(id=seed_id).users.add(user_id)
  return redirect('seeds_detail', seed_id=seed_id)

def remove_seed(request, seed_id, user_id):
  Seed.objects.get(id=seed_id).users.remove(user_id)
  print(f'You removed user {user_id} from this seed: {seed_id}')
  return redirect('seeds_detail', seed_id=seed_id)
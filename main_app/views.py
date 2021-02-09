from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Profile, User, Seed, Note, Conversation, Message, Garden, Todo
from .forms import UserForm, SeedCreateForm, NoteCreateForm, MessageCreateForm, ReplyForm, TodoForm
# from PIL import Image
# Create your views here.

def home(request):
  return render(request, 'home.html')

def users_index(request):
  users = User.objects.all()
  print(users)
  return render(request, 'users/index.html', {'users': users})

def users_detail(request, userName_id):
  userWhoOwnsProfile = User.objects.get(id=userName_id)
  profile = Profile.objects.get(user=userName_id)
  friends = profile.friends.all()
  loggedInUserProfile = Profile.objects.get(user_id=request.user.id)
  if loggedInUserProfile.friends.filter(id=profile.id):
    print('User is friends with this person already')
    is_friend = True
  else:
    print('User is not friends with this person yet')
    is_friend = False
  return render(request, 'users/detail.html', { 'userAssociatedWithProfile': userWhoOwnsProfile, 'profile': profile, 'is_friend':is_friend, 'friends': friends })

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
      new_garden = Garden.objects.create()
      new_garden.user_id = user.id
      print(new_garden)
      print(new_garden.user_id)
      new_garden.save()
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
  form = SeedCreateForm(request.POST)
  context = {'form': form}
  if form.is_valid():
    new_seed = form.save()
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

def conversations_index(request):
  conversations = Conversation.objects.filter(participants=request.user)
  print(conversations)
  return render(request, 'conversations/index.html', {'conversations': conversations})

def conversations_detail(request, conversation_id):
  conversation = Conversation.objects.get(id=conversation_id)
  print(conversation)
  reply_form = ReplyForm()
  return render(request, 'conversations/detail.html', {'conversation': conversation, 'reply_form': reply_form})

def messages_create(request):
  form = MessageCreateForm(request.POST)
  context = {'form': form}
  if form.is_valid():
    new_message = form.save(commit=False)
    new_message.sender_id = request.user.id
    existing_conversation = Conversation.objects.filter(participants = request.user and new_message.recipient)
    if existing_conversation:
      new_message.conversation_id = existing_conversation[0].id
      print(new_message.conversation_id)
    else:
      new_conversation = Conversation.objects.create()
      # print(new_conversation)
      new_conversation.participants.add(request.user.id, new_message.recipient.id)
      new_message.conversation_id = new_conversation.id
    # print(new_message.conversation_id)
    new_message.save()
    return redirect('conversations_detail', conversation_id=new_message.conversation_id)
  return render(request, 'conversations/create_message.html', context)

def conversations_reply(request, conversation_id):
  form = ReplyForm(request.POST)
  if form.is_valid():
    conversation = Conversation.objects.get(id=conversation_id)
    new_message = form.save(commit=False)
    new_message.sender_id = request.user.id
    findRecipient = conversation.participants.exclude(id=request.user.id)
    recipient = User.objects.get(id=findRecipient[0].id)
    new_message.recipient_id = recipient.id
    new_message.conversation_id = conversation.id
    new_message.save()
  return redirect('conversations_detail', conversation_id=conversation_id)

def share_seed(request, seed_id):
  form = MessageCreateForm(request.POST)
  seed = Seed.objects.get(id=seed_id)
  context = {'form': form, 'seed': seed}
  if form.is_valid():
    new_message = form.save(commit=False)
    new_message.sender_id = request.user.id
    if seed_id:
      new_message.seed_id = seed_id
    existing_conversation = Conversation.objects.filter(participants = request.user and new_message.recipient)
    if existing_conversation:
      new_message.conversation_id = existing_conversation[0].id
      print(new_message.conversation_id)
    else:
      new_conversation = Conversation.objects.create()
      new_conversation.participants.add(request.user.id, new_message.recipient.id)
      new_message.conversation_id = new_conversation.id
    new_message.save()
    return redirect('conversations_detail', conversation_id=new_message.conversation_id)
  return render(request, 'conversations/create_message.html', context)

def garden_detail(request, user_id):
  garden = Garden.objects.get(user_id=user_id)
  todos = Todo.objects.filter(user_id=user_id)
  seeds = garden.seeds.all()
  print(seeds)
  todo_form = TodoForm()
  return render(request, 'garden/details.html', {'garden': garden, 'todos': todos, 'todo_form': todo_form, 'seeds': seeds})

def add_todo(request, garden_id):
  form = TodoForm(request.POST)
  if form.is_valid():
    new_todo = form.save(commit=False)
    new_todo.garden_id = garden_id
    new_todo.user_id = request.user.id
    new_todo.save()
  return redirect('garden_detail', user_id=request.user.id)

def delete_todo(request, garden_id, todo_id):
  Todo.objects.filter(id=todo_id).delete()
  return redirect('garden_detail', user_id=request.user.id)

def grow_seed(request, user_id, seed_id):
  garden = Garden.objects.get(user_id=user_id)
  garden.seeds.add(seed_id)
  return redirect('seeds_detail', seed_id=seed_id)
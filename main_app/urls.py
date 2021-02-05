from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/createprofile/', views.ProfileCreate.as_view(), name='create_profile'),
  path('users/', views.users_index, name='users_index'),
  path('users/<int:userName_id>/', views.users_detail, name='users_detail'),
  path('users/<int:pk>/updateprofile/', views.ProfileUpdate.as_view(), name='update_profile'),
  path('users/<int:profile_id>/addfriend/<int:otheruser_id>', views.add_friend, name='add_friend'),
  path('seeds/create', views.seed_create, name='seeds_create'),
  path('seeds/', views.seed_list, name='seeds_list'),
  path('seeds/<int:seed_id>/', views.seeds_detail, name='seeds_detail'),
  path('seeds/<int:seed_id>/addnote/', views.add_note, name='add_note'),
  path('seeds/<int:seed_id>/saveseed/<int:user_id>', views.save_seed, name='save_seed'),
]
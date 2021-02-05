from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/createprofile/', views.ProfileCreate.as_view(), name='create_profile'),
  path('users/', views.users_index, name='users_index'),
  path('users/<int:user_id>/', views.users_detail, name='users_detail'),
  path('seeds/create', views.seed_create, name='seeds_create'),
  path('seeds/', views.seed_list, name='seeds_list'),
  path('seeds/<int:seed_id>/', views.seeds_detail, name='seeds_detail'),
]
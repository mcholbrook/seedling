from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/createprofile/', views.ProfileCreate.as_view(), name='create_profile'),
  path('users/', views.users_index, name='users_index'),
  path('users/<int:user_id>/', views.users_detail, name='users_detail'),
  path('seeds/create', views.SeedCreate, name='seed_create'),
]
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import ProfileDetails,  CreateCustomUser, EditProfile, DeleteUser


urlpatterns = [
  path('',include('django.contrib.auth.urls')),
  path('profile/', login_required(ProfileDetails.as_view()), name='accounts.profile'),
  path('logout/', LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
  path('register', CreateCustomUser.as_view(), name='accounts.create'),
  path('<int:pk>/edit', login_required(EditProfile.as_view()), name='profile.edit'),
  path('<int:pk>/delete', login_required(DeleteUser.as_view()), name='profile.delete')
]
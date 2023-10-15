from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from accounts.forms import CustomizedUserCreationForm

# Create your views here.

class ProfileDetails(DetailView):
  model = User
  template_name = 'accounts/profile.html'
  context_object_name = 'profile'

  def get_object(self, queryset=None):
      return self.request.user

class CreateCustomUser(CreateView):
  model = User
  template_name = 'accounts/registeration.html'
  form_class = CustomizedUserCreationForm
  success_url = reverse_lazy("login")

class EditProfile(UpdateView):
  model = User
  template_name = 'accounts/edit.html'
  form_class = CustomizedUserCreationForm
  success_url = reverse_lazy('login')

class DeleteUser(DeleteView):
  model = User
  template_name = 'accounts/delete.html'
  success_url = reverse_lazy('accounts.create')
  
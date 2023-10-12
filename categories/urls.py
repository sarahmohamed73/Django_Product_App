from django.urls import path
from categories.views import index, details

urlpatterns = [
  path('',index, name='categories.index'),
  path('details/<int:id>', details, name='categories.details'),
]
from django.urls import path
from amazon.views import index, details, delete, search, contact_us, about_us, createViaForm, editViaForm

urlpatterns = [
  path('',index, name='amazon.index'),
  path('details/<int:id>', details, name='amazon.detail'),
  path('<int:id>/delete', delete, name='amazon.delete'),
  path('search/', search, name='amazon.search'),
  path('contactus/', contact_us, name='amazon.contactus'),
  path('aboutus/', about_us, name='amazon.aboutus'),
  path('forms/create', createViaForm, name='amazon.createform'),
  path('<int:id>/forms/edit', editViaForm, name='amazon.editform'),
]
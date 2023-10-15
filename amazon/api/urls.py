from django.urls import path
from amazon.api.view import index, student_resourse

urlpatterns = [
  path('', index, name='api.index'),
  path('<int:id>', student_resourse, name='api.student_resourse')
]
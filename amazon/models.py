from django.db import models
from django.shortcuts import reverse
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(null=True, blank=True)
  price = models.FloatField()
  stock = models.IntegerField()
  image = models.ImageField(upload_to='amazon/images/', blank=True, null=True)
  owner = models.ForeignKey(User, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='owner')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  category = models.ForeignKey(Category, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='amazon')


  def __str__(self):
    return f"{self.name}"
  
  @classmethod
  def get_all_products(cls):
    return  cls.objects.all()


  def get_image_url(self):
    return f"/media/{self.image}"
  
  def get_detail_url(self):
    return  reverse('amazon.detail', args=[self.id])


  def get_delete_url(self):
    return  reverse('amazon.delete', args=[self.id])
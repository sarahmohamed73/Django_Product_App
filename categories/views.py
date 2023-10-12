from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from categories.models import Category
# Create your views here.

def index(request):
  categories= Category.get_all_categories()
  return render(request, 'categories/index.html', context={"categories":categories})

def details(request, id):
  category = get_object_or_404(Category, pk=id)
  return render(request, 'categories/category.html', context={"category":category})
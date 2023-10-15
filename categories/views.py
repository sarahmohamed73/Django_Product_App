from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from categories.models import Category
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def index(request):
  categories= Category.get_all_categories()
  return render(request, 'categories/index.html', context={"categories":categories})

@login_required()
def details(request, id):
  category = get_object_or_404(Category, pk=id)
  return render(request, 'categories/category.html', context={"category":category})
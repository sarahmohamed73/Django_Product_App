from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.http import HttpResponse
from amazon.models import Product
from categories.models import Category
from amazon.form import ProductForm
# Create your views here.

def index(request):
  products = Product.objects.all()
  return render(request, 'amazon/index.html', context={"products":products})

def details(request, id):
  product = get_object_or_404(Product, pk=id)
  return render(request, 'amazon/product.html', context={"product":product})

def delete(request, id ):
    product = Product.objects.get(id=id)
    product.delete()
    url = reverse('amazon.index')
    return redirect(url)

def search(request):
    search_query = request.GET.get('search')
    products = Product.objects.filter(name__istartswith=search_query)
    return render(request, 'amazon/search.html', {'products': products})

def contact_us(request):
  return render(request, 'amazon/contactus.html')

def about_us(request):
  return render(request, 'amazon/aboutus.html')

def createViaForm(request):
  form = ProductForm()
  if request.POST:
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
      name = request.POST['name']
      description = request.POST['description']
      price = request.POST['price']
      stock = request.POST['stock']
      image = None
      if "image" in request.FILES:
        image = request.FILES['image']
      category = None
      if request.POST['category']:
        category = Category.objects.get(id=request.POST['category']) 
      product = Product.objects.create(name=name, description=description, price=price, stock=stock, image=image, category=category)
      return redirect(product.get_detail_url())
  return  render(request, 'amazon/forms/create.html', context={"form":form})

def editViaForm(request, id):
  product = get_object_or_404(Product, id=id)
  form = ProductForm(instance=product)
  if request.POST:
    form = ProductForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
      product.name = request.POST['name']
      product.description = request.POST['description']
      product.price = request.POST['price']
      product.stock = request.POST['stock']
      product.image = None
      if "image" in request.FILES:
        product.image = request.FILES['image']
      product.category = None
      if request.POST['category']:
        product.category = Category.objects.get(id=request.POST['category']) 
      product.save()
      return redirect(product.get_detail_url())
  return render(request, 'amazon/forms/edit.html', {'form': form, 'product': product})

from rest_framework.response import Response
from rest_framework.decorators import api_view
from amazon.models import Product
from amazon.api.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def index(request):
  if request.method == 'POST':
    product = ProductSerializer(data=request.data)
    if product.is_valid():
      product.save()
      return Response({'message': 'Product Added Successfully', 'product':product.data}, status=201)
    return Response(product.errors, status=400)
  
  elif request.method == 'GET':
    products = Product.get_all_products()
    serialized_products = ProductSerializer(products, many = True)
    return Response({'message': 'Products Data Receieved Successfully', 'products': serialized_products.data}, status=200)
  
@api_view(['GET', 'DELETE', 'PUT'])
def student_resourse(request, id):
  product = Product.objects.filter(id=id).first()

  if request.method == 'GET':
    serialized_product = ProductSerializer(product)
    return Response({'message': 'Product Data Receieved Successfully', 'product': serialized_product.data}, status=200)
  
  elif request.method == 'PUT':
    serialized_product = ProductSerializer(instance=product, data=request.data)
    if serialized_product.is_valid():
      serialized_product.save()
      return Response({'message': 'Product Updated Successfully', 'product': serialized_product.data}, status=201)
    return Response(serialized_product.errors, status=400)
  
  elif request.method == 'DELETE':
    product.delete()
    return Response({'message': 'Product Deleted Successfully'}, status= 204)

from rest_framework import serializers
from amazon.models import Product
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField(max_length=100,validators=[UniqueValidator(queryset=Product.objects.all())])
  description = serializers.CharField(max_length=1000, allow_null=True)
  price = serializers.FloatField()
  stock = serializers.IntegerField()
  image = serializers.ImageField(required=False)
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)

  def create(self, validate_data):
    return Product.objects.create(**validate_data)
  
  def update(self, instance, validated_data):
    instance.name = validated_data.get('name')
    instance.description = validated_data.get('description')
    instance.price = validated_data.get('price')
    instance.stock = validated_data.get('stock')
    instance.image = validated_data.get('image')
    instance.save()
    return instance
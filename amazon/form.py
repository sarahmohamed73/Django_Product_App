from django import  forms
from amazon.models import Product
from categories.models import Category
from django.core.exceptions import ValidationError

class ProductForm(forms.Form):
  name = forms.CharField()
  description = forms.CharField(required=False)
  price = forms.FloatField()
  stock = forms.IntegerField()
  image = forms.ImageField(required=False)
  category  = forms.ModelChoiceField(Category.get_all_categories(), required=False)

  def __init__(self, *args, **kwargs):
    self.instance = kwargs.pop('instance', None)
    super().__init__(*args, **kwargs)
    if self.instance:
      self.fields['name'].initial = self.instance.name
      self.fields['description'].initial = self.instance.description
      self.fields['price'].initial = self.instance.price
      self.fields['stock'].initial = self.instance.stock
      self.fields['category'].initial = self.instance.category

  def clean_name(self):
    name = self.cleaned_data['name']
    if self.instance and self.instance.name == name:
      return name
    found = Product.objects.filter(name=name).exists()
    if found:
      raise ValidationError("This product already exists.")
    return name
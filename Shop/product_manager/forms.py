from django import forms
from .models import Product, Category, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'description', 'price', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
		

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'goods', 'quantity', 'date']




from django.contrib import admin
from django import forms
from .models import Product, Category, Order



class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['name', 'slug', 'quantity', 'description', 'price']
    readonly_fields = ['slug']

admin.site.register(Product, ProductAdmin)


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

admin.site.register(Category, CategoryAdmin)

class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
		
class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ['name', 'slug', 'quantity', 'date']
    readonly_fields = ['slug']

admin.site.register(Order, OrderAdmin)
	




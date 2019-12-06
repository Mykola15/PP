from django.urls import include, path, re_path
from rest_framework import routers
from django.urls import path
from .views import *
from . import views

urlpatterns = (
    # urls for Product
    path('product/', views.IndexView.as_view(), name='index'),
    path('product/list/', views.ProductListView.as_view(), name='product_manager_product_list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_manager_product_create'),
    path('product/detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_manager_product_detail'),
    path('product/update/<slug:slug>/', views.ProductUpdateView.as_view(), name='product_manager_product_update'),
    path('product/delete/<slug:slug>/', views.ProductDeleteView.as_view(), name='product_manager_product_delete'),
)

urlpatterns += (
    # urls for Category
    path('category/', views.CategoryListView.as_view(), name='product_manager_category_list'),
    path('category/detail/<slug:slug>/', views.CategoryDetailView.as_view(), name='product_manager_category_detail'),
)

urlpatterns += (
    # urls for Order
	path('order/', views.Index1View.as_view(), name='index1'),
    path('order/list/', views.OrderListView.as_view(), name='product_manager_order_list'),
    path('order/create/', views.OrderCreateView.as_view(), name='product_manager_order_create'),
    path('order/detail/<slug:slug>/', views.OrderDetailView.as_view(), name='product_manager_order_detail'),
    path('order/update/<slug:slug>/', views.OrderUpdateView.as_view(), name='product_manager_order_update'),
    path('order/delete/<slug:slug>/', views.OrderDeleteView.as_view(), name='product_manager_order_delete'),
)







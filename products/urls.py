# urls.py
from django.urls import path
from .views import ProductAPIView, ProductDetailAPIView, LatestProductsAPIView, Show_all, Show_Category, product_details, SearchProduct

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('show/latest/', LatestProductsAPIView.as_view(), name='latest-products'),
    path('show/all/', Show_all.as_view(), name='show-all-products'),
    path('show/category/<str:category>/', Show_Category.as_view(), name='show-category-products'),
    path('products/details/<int:pk>/', product_details.as_view(), name='product-details'),
    path('products/search/<str:query>/', SearchProduct.as_view(), name='search-products'),

]

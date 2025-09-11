from django.db import models

# Create your models here.
class Product(models.Model):
    """Model representing a product in the e-commerce platform."""
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    CATEGORY_CHOICES = [
    ('Bags', 'Bags'),
    ('Shoes', 'Shoes'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    

class ProductImage(models.Model):
    """Model representing images associated with a product."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='product_images/')

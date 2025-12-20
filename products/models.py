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
    ('Belts', 'Belts'),
    ('Leather Jackets', 'Leather Jackets'),
    ('Suit Jackets', 'Suit Jackets'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    

class ProductImage(models.Model):
    """Model representing images associated with a product."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='product_images/')


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    cash_on_delivery = models.BooleanField(default=False)
    
    STATUS_CHOICES = (
        ('Placed', 'Placed'),
        ('Confirmed', 'Confirmed'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Placed')

    products = models.ManyToManyField(
        Product,
        through='OrderItem',
        related_name='orders'
    )

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    

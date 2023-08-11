from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # products

class Collection(models.Model):# defined before product to reference
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')# Resolve circular dependancy with product. If product is deleted, change to null value. related_name='+' to not create reverse relationship.
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField() # SEO technique. Make engines find content easier.
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True) # add current time when a new product is created
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) # Implement a one to many relationship. Creates foreign key.
    promotions = models.ManyToManyField(Promotion) # Many to many relationship. Plural because you want to return all promotions that are relevant to product
    
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    
        
    
class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'
    
    PAYMENT_CHOICES = [
        (PAYMENT_PENDING, 'Payment pending'),
        (PAYMENT_COMPLETE, 'Payment Comolete'),
        (PAYMENT_FAILED, 'Payment failed'),
    ]
    
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT) # Should never delete orders from db. Represent sales
    
class OrderItem(models.Model):# Association class
    order = models.ForeignKey(Order, on_delete=models.PROTECT) # OrderItems should not be deleted
    product = models.ForeignKey(Product, on_delete=models.PROTECT) # associated OrderItem should not be deleted
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) # Price already in products but can change over time. Store at time of order
    
    
class Address(models.Model): # Child of Customer class
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) #Implement a one to one relationship
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)# Items should be deleted if Cart is deleted
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    
    
    
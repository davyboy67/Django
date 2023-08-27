from django.shortcuts import render
from django.db import transaction
from store.models import Product, Collection, Order, OrderItem

def say_hello(request):
    
    Order.objects.filter(pk__gt=1001).delete()
    #...
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()
        
        item = OrderItem()
        item.order = order
        item.product_id = -1
        item.quantity = 1
        item.unit_price = 1
        item.save()
    
    
    
    return render(request, 'hello.html', { 'name': 'Mosh'})
    

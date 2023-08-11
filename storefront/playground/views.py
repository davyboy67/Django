from django.shortcuts import render
from django.db.models import Q, F
from django.db.models import Sum, Count, Avg, Min, Max
from store.models import Product, OrderItem, Order
from store.models import Customer

def say_hello(request):
    # keyword=value
    #
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # queryset = Product.objects.filter(Q(unit_price__gt=70) & Q(unit_price__lt=90)).order_by('title')[15:30]
    # queryset =  Product.objects.filter(id__in= OrderItem.objects.values('product_id').distinct()).order_by('title')
    #queryset = Product.objects.select_related('collection').all() 
    #queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    #select_related - other end of relationship has one instance
    #prefetch_related - other end of relationship has many instances
    result = Order.objects.aggregate(count=Count('id'))
    result1 = OrderItem.objects.filter(product__id=1).aggregate(units_sold=Count('quantity'))
    result2 = Order.objects.filter(customer__id=1).aggregate(orders_placed=Count('id'))
    
    
    #queryset = Product.objects.values('id', 'title', 'orderitem__product_id').order_by('title') #inner join. 
        
    return render(request, 'hello.html', { 'name': 'Mosh', 'result': result, 'result1': result1, 'result2': result2, 'result3': result3  })
    

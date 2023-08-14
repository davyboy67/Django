from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
    #find the content type id for product model
    Tags = TaggedItem.objects.get_tags_for(Product, 1)
    
    #queryset = Product.objects.values('id', 'title', 'orderitem__product_id').order_by('title') #inner join. 
        
    return render(request, 'hello.html', { 'name': 'Mosh', 'tags': Tags})
    

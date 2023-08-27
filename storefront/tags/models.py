from django.db import models
from django.contrib.contenttypes.models import ContentType # specifically made for allowing generic relationships
from django.contrib.contenttypes.fields import GenericForeignKey
from store.models import Product
# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)
     
class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        #find the content type id for product model
        content_type = ContentType.objects.get_for_models(obj_type) 
        #queryset = Product.objects.values('id', 'title', 'orderitem__product_id').order_by('title') #inner join. 
        return TaggedItem.objects.select_related('tag').filter(content_type = content_type, object_id=obj_id)
    

class TaggedItem(models.Model):
    objects = TaggedItemManager() 
    #What tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (product, video, article) - generic way to identify object in database
    # ID. Identify any record in any tables with these two fields.
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey # read actual object particular tag is applied to
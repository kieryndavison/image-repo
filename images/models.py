from django.db import models
from django.utils.html import mark_safe


# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def image_view(self):
        if self.image:
            return mark_safe('<img src="{0}" width="100" height="100" style="object-fit:contain" />'.format(self.image.url))
        else:
            return 'No image found'

    image_view.short_description = 'Image preview'

    def price_view(self):
        return '%.2f' % self.price

    price_view.short_description = "Price"

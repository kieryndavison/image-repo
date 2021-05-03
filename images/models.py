from django.db import models
from django.utils.html import mark_safe, format_html


# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)

    def image_view(self):
        if self.image:
            return mark_safe('<img src="{0}" width="100" style="object-fit:contain" />'.format(self.image.url))
        else:
            return 'No image found'
    image_view.short_description = 'Image preview'

    def price_view(self):
        return '%.2f' % (self.price * (1 - self.discount))
    price_view.short_description = "Discounted Price"

    def discount_view(self):
        return '%.0f%%' % (self.discount * 100)
    discount_view.short_description = "Discount"

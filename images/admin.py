from django.contrib import admin
from .models import Image

# Register your models here.

# Display all image fields in the admin table, inculding custom image, discount and price views

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_view', 'desc', 'owner', 'price', 'discount_view', 'price_view', 'stock')

admin.site.register(Image, ImageAdmin)

from django.contrib import admin
from .models import Image

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_view', 'desc', 'price', 'discount_view', 'price_view', 'stock', 'image_actions')

admin.site.register(Image, ImageAdmin)

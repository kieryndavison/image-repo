from django.test import TestCase
from .models import Image
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your tests here.

class ImageTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        Image.objects.create(name="book", image="pics/book_cvPQFCS.jpeg", desc="test", price=232.34, discount=0.32, stock=7, owner=user)
        Image.objects.create(name="congrats", desc="test", price=232.34, discount=0.21, stock=4, owner=user)

    def test_image_is_formated_correctly(self):
        """Image formated with html"""
        book = Image.objects.get(name="book")
        self.assertEqual(book.image_view(), mark_safe('<img src="{0}" width="100" style="object-fit:contain" />'.format(book.image.url)))

    def test_image_not_found(self):
        """Image not found returned if no image exists"""
        congrats = Image.objects.get(name="congrats")
        self.assertEqual(congrats.image_view(), 'No image found')
    
    def test_discount_is_formated_correctly(self):
        """Image discount is formated into percentage"""
        book = Image.objects.get(name="book")
        congrats = Image.objects.get(name="congrats")
        self.assertEqual(book.discount_view(), '%.0f%%' % (book.discount * 100))
        self.assertEqual(congrats.discount_view(), '%.0f%%' % (congrats.discount * 100))
    
    def test_price_is_calculated_correctly(self):
        """Image price is calculated from discount"""
        book = Image.objects.get(name="book")
        congrats = Image.objects.get(name="congrats")
        self.assertEqual(book.price_view(), '%.2f' % (book.price * (1 - book.discount)))
        self.assertEqual(congrats.price_view(), '%.2f' % (congrats.price * (1 - congrats.discount)))
from django.test import TestCase
from .models import Image
from django.contrib.auth.models import User
from .views import ImageViewSet
from rest_framework import status
from rest_framework.test import APIRequestFactory


class ImageTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.image = Image.objects.create(name="book", image="pics/book_cvPQFCS.jpeg", desc="test", price=232.34, discount=0.32, stock=7, owner=self.user)

    def test_creating_image(self):
        # Create an instance of a GET request.
        request = self.factory.post('/images/', {'name': 'book', 'image': 'pics/book_cvPQFCS.jpeg', 'desc': 'test', 'price': '232.34', 'discount': '0.32', 'stock': '7', 'owner': 'testuser'}, format='json')
        request.user = self.user

        response = ImageViewSet.as_view({'post': 'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_get_image_list(self):
        # Create an instance of a GET request.
        request = self.factory.get('/images')

        response = ImageViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
    
    def test_get_image_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/images/1')

        response = ImageViewSet.as_view({'get': 'retrieve'})(request, pk=self.image.id)
        response.render()  # Cannot access `response.content` without this.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, {'name': 'book', 'image': 'pics/book_cvPQFCS.jpeg', 'desc': 'test', 'price': '232.34', 'discount': '0.32', 'stock': '7', 'owner': 'testuser'})
from django.test import TestCase
from .models import Image
from django.contrib.auth.models import User, AnonymousUser
from .views import ImageViewSet, UserViewSet
from rest_framework import status
from rest_framework.test import APIRequestFactory

class ImageViewSetTest(TestCase):
    """ImageViewSet has both read and write permissions, therefore we test POST, PUT, DELETE and GET methods"""
    def setUp(self):
        self.factory = APIRequestFactory()
        self.object_owner_user = User.objects.create_user(username='testuser', password='12345')
        self.non_object_owner_user = User.objects.create_user(username='testuser1', password='12345')
        self.image = Image.objects.create(name="book", image="pics/book_cvPQFCS.jpeg", desc="test", price=232.34, discount=0.32, stock=7, owner=self.object_owner_user)
    
    # Test image post request
    def test_creating_image(self):
        request = self.factory.post('/images/', {'name': 'book', 'image': 'pics/book_cvPQFCS.jpeg', 'desc': 'test', 'price': '232.34', 'discount': '0.32', 'stock': '7'}, format='json')
        request.user = self.object_owner_user

        response = ImageViewSet.as_view({'post': 'list'})(request)
        self.assertEqual(response.status_code, 200)
    
    # Test image put requests - only image owner should have permission update
    def test_updating_image_owned_by_user(self):
        request = self.factory.put('/images/{self.image.id}', {'name': 'test'}, format='json')
        request.user = self.object_owner_user

        response = ImageViewSet.as_view({'put': 'retrieve'})(request, pk=self.image.id)
        self.assertEqual(response.status_code, 200)
    
    def test_updating_image_not_owned_by_user(self):
        request = self.factory.put('/images/{self.image.id}', {'name': 'test'}, format='json')
        request.user = self.non_object_owner_user

        response = ImageViewSet.as_view({'put': 'retrieve'})(request, pk=self.image.id)
        self.assertEqual(response.status_code, 403)
    
    # Test image delete requests - only image owner should have permission delete
    def test_deleting_image_owned_by_user(self):
        request = self.factory.delete('/images/{self.image.id}')
        request.user = self.object_owner_user

        response = ImageViewSet.as_view({'delete': 'retrieve'})(request, pk=self.image.id)
        self.assertEqual(response.status_code, 200)
    
    def test_deleting_image_not_owned_by_user(self):
        request = self.factory.delete('/images/{self.image.id}')
        request.user = self.non_object_owner_user

        response = ImageViewSet.as_view({'delete': 'retrieve'})(request, pk=self.image.id)
        self.assertEqual(response.status_code, 403)

    # Test getting all images
    def test_get_image_list(self):
        request = self.factory.get('/images')

        response = ImageViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
    
    # Test getting a specific image
    def test_get_image_details(self):
        request = self.factory.get('/images/{self.image.id}')

        response = ImageViewSet.as_view({'get': 'retrieve'})(request, pk=self.image.id)
        self.assertEqual(response.status_code, 200)

class UserViewSetTest(TestCase):
    """UserViewSet has both only read permissions, therefore we test only GET methods"""
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')

    # Test getting all users
    def test_get_user_list(self):
        request = self.factory.get('/users')

        response = UserViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
    
    # Test getting a specific user
    def test_get_user_details(self):
        request = self.factory.get('/users/{self.user.id}')

        response = UserViewSet.as_view({'get': 'retrieve'})(request, pk=self.user.id)
        self.assertEqual(response.status_code, 200)

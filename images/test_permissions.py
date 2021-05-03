from django.test import TestCase
from .models import Image
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.test import APIRequestFactory

class IsOwnerOrReadOnlyTestCase(TestCase):
    """Ensure that only image owners have write/delete permissions"""
    def setUp(self):
        self.factory = APIRequestFactory()
        self.object_owner_user = User.objects.create_user(username='testuser', password='12345')
        self.non_object_owner_user = User.objects.create_user(username='testuser1', password='12345')
        Image.objects.create(name="book", image="pics/book_cvPQFCS.jpeg", desc="test", price=232.34, discount=0.32, stock=7, owner=self.object_owner_user)

    # Image owner should have write, delete and read permissions
    def test_delete_permissions_when_user_is_owner(self):
        book = Image.objects.get(name="book")
        request = self.factory.delete('/')
        request.user = self.object_owner_user

        permission_check = IsOwnerOrReadOnly()
        permission = permission_check.has_object_permission(request, None, book)
        self.assertTrue(permission)

    def test_put_permissions_when_user_is_owner(self):
        book = Image.objects.get(name="book")
        request = self.factory.put('/')
        request.user = self.object_owner_user

        permission_check = IsOwnerOrReadOnly()
        permission = permission_check.has_object_permission(request, None, book)
        self.assertTrue(permission)
    
    def test_get_permissions_when_user_is_owner(self):
        book = Image.objects.get(name="book")
        request = self.factory.get('/')
        request.user = self.object_owner_user

        permission_check = IsOwnerOrReadOnly()
        permission = permission_check.has_object_permission(request, None, book)
        self.assertTrue(permission)
    
    # Users that are not the image owner should have only read permissions
    def test_delete_permissions_when_user_is_not_owner(self):
        book = Image.objects.get(name="book")
        request = self.factory.delete('/')
        request.user = self.non_object_owner_user

        permission_check = IsOwnerOrReadOnly()
        permission = permission_check.has_object_permission(request, None, book)
        self.assertFalse(permission)
    
    def test_put_permissions_when_user_is_not_owner(self):
        book = Image.objects.get(name="book")
        request = self.factory.put('/')
        request.user = self.non_object_owner_user

        permission_check = IsOwnerOrReadOnly()
        permission = permission_check.has_object_permission(request, None, book)
        self.assertFalse(permission)
    
    def test_get_permissions_when_user_is_not_owner(self):
        book = Image.objects.get(name="book")
        request = self.factory.get('/')
        request.user = self.non_object_owner_user

        permission_check = IsOwnerOrReadOnly()
        permission = permission_check.has_object_permission(request, None, book)
        self.assertTrue(permission)
    
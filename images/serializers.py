from rest_framework import serializers
from .models import Image
from django.contrib.auth.models import User

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Image
        fields = ['name', 'image', 'desc', 'owner', 'price', 'discount', 'stock']

class UserSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'images']
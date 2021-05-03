from rest_framework import serializers
from .models import Image
from django.contrib.auth.models import User

class ImageSerializer(serializers.ModelSerializer):
    # Do not allow user to modity the owner field  
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Image
        fields = ['url', 'id', 'name', 'image', 'desc', 'owner', 'price', 'discount', 'stock']

class UserSerializer(serializers.ModelSerializer):
    # Link to the image detail view   
    images = serializers.HyperlinkedRelatedField(many=True, view_name='image-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'images']

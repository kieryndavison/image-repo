from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register viewsets with it
router = DefaultRouter()
router.register(r'images', views.ImageViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]

# Add login functionality
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

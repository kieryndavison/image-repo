from django.shortcuts import render
from .models import Image
from .serializers import ImageSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User


# Create your views here.

# def home(request):
#     images = Image.objects.all()

#     return render(request, 'home.html', {'images': images})

class ImageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     image = self.get_object()
    #     return Response(image.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
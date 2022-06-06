from rest_framework import viewsets

# import local data
from .serializers import BlogPostSerializer, BlogPostDetailSerializer
from .models import BlogPost


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogDetailViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer

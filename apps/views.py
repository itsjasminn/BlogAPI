from drf_spectacular.utils import extend_schema
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import Blog, BlogImages
from apps.serializers import BlogModelSerializer, BlogImagesModelSerializer


# Create your views here.


@extend_schema(tags=['blog'])
class BlogDestroyAPIView(DestroyAPIView):
    serializer_class = BlogModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog'])
class BlogUpdateAPIView(UpdateAPIView):
    serializer_class = BlogModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog'])
class BlogDetailAPIView(RetrieveAPIView):
    serializer_class = BlogModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog-images'])
class BlogImagesCreateAPIView(CreateAPIView):
    serializer_class = BlogImagesModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = BlogImages.objects.all()


@extend_schema(tags=['blog-images'])
class BlogImagesUpdateAPIView(UpdateAPIView):
    serializer_class = BlogImagesModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = BlogImages.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog-images'])
class BlogImagesDetailAPIView(RetrieveAPIView):
    serializer_class = BlogImagesModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = BlogImages.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog-images'])
class BlogImagesDestroyAPIView(DestroyAPIView):
    serializer_class = BlogImagesModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = BlogImages.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog-images'])
class BlogImagesListAPIView(ListAPIView):
    serializer_class = BlogImagesModelSerializer
    queryset = BlogImages.objects.all()
    permission_classes = [IsAuthenticated]


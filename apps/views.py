from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import Blog
from apps.serializers import BlogModelSerializer


@extend_schema(tags=['blog'])
class BlogCreateAPIView(CreateAPIView):
    serializer_class = BlogModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(tags=['blog'])
class BlogListAPIView(ListAPIView):
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]


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

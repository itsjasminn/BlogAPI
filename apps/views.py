from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from apps.models import Blog, BlogImages, Comment
from apps.serializers import BlogModelSerializer, BlogImagesModelSerializer, CommentModelSerializer


@extend_schema(tags=['blog'])
class BlogCreateAPIView(CreateAPIView):
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(tags=['blog'])
class BlogListAPIView(ListAPIView):
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()


@extend_schema(tags=['blog'])
class BlogDestroyAPIView(DestroyAPIView):
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog'])
class BlogUpdateAPIView(UpdateAPIView):
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog'])
class BlogDetailAPIView(RetrieveAPIView):
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog-images'])
class BlogImagesCreateAPIView(CreateAPIView):
    serializer_class = BlogImagesModelSerializer
    queryset = BlogImages.objects.all()


@extend_schema(tags=['blog-images'])
class BlogImagesUpdateAPIView(UpdateAPIView):
    serializer_class = BlogImagesModelSerializer
    queryset = BlogImages.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog-images'])
class BlogImagesDetailAPIView(RetrieveAPIView):
    serializer_class = BlogImagesModelSerializer
    queryset = BlogImages.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog-images'])
class BlogImagesDestroyAPIView(DestroyAPIView):
    serializer_class = BlogImagesModelSerializer
    queryset = BlogImages.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['blog-images'])
class BlogImagesListAPIView(ListAPIView):
    serializer_class = BlogImagesModelSerializer
    queryset = BlogImages.objects.all()


# ==================================================================


@extend_schema(tags=['block-comment'])
class CommentCreatAPIView(CreateAPIView):
    serializer_class = CommentModelSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(tags=['block-comment'])
class CommentListAPIView(ListAPIView):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        query = super().get_queryset()
        pk = self.kwargs.get('pk')
        query = query.filter(blog_id=pk).all()
        return query

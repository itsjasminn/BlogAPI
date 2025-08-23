from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from apps.models import Blog, BlogImages, Question
from apps.serializers import BlogModelSerializer, BlogImagesModelSerializer, QuestionModelSerializer


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


@extend_schema(tags=['question'])
class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionModelSerializer
    queryset = Question.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(tags=['question'])
class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionModelSerializer
    queryset = Question.objects.all()


@extend_schema(tags=['question'])
class QuestionDeleteAPIView(DestroyAPIView):
    serializer_class = QuestionModelSerializer
    queryset = Question.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['question'])
class QuestionUpdateAPIView(UpdateAPIView):
    serializer_class = QuestionModelSerializer
    queryset = Question.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['question'])
class QuestionDetailAPIView(RetrieveAPIView):
    serializer_class = QuestionModelSerializer
    queryset = Question.objects.all()
    lookup_field = 'pk'

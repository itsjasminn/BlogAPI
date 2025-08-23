from http import HTTPStatus

from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, \
    GenericAPIView
from rest_framework.response import Response

from apps.models import Blog, BlogImages, Comment, Question, Answer, AnswerComment
from apps.serializers import BlogModelSerializer, BlogImagesModelSerializer, CommentModelSerializer, LikeSerializer, \
    QuestionModelSerializer, AnswerModelSerializer, AnswerCommentModelSerializer
from apps.models import Blog, BlogImages, Comment, Question
from apps.serializers import BlogModelSerializer, BlogImagesModelSerializer, CommentModelSerializer, LikeSerializer, \
    VotesSerializer


@extend_schema(tags=['blog'])
class BlogCreateAPIView(CreateAPIView):
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(tags=['blog'])
class BlogLikeGenericAPIView(GenericAPIView):
    serializer_class = LikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.blog_data
        blog.likes.add(request.user)
        return Response({'message': 'like bosildi'}, status=HTTPStatus.OK)


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


@extend_schema(tags=['answers'])
class AnswerCreateAPIView(CreateAPIView):
    serializer_class = AnswerModelSerializer
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(tags=['answers'])
class AnswerListAPIView(ListAPIView):
    serializer_class = AnswerModelSerializer
    queryset = Answer.objects.all()


@extend_schema(tags=['answers'])
class AnswerDeleteAPIView(DestroyAPIView):
    serializer_class = AnswerModelSerializer
    queryset = Answer.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['answers'])
class AnswerUpdateAPIView(UpdateAPIView):
    serializer_class = AnswerModelSerializer
    queryset = Answer.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['answers'])
class AnswerDetailAPIView(RetrieveAPIView):
    serializer_class = AnswerModelSerializer
    queryset = Answer.objects.all()
    lookup_field = 'pk'
# ==================================================================Comment


@extend_schema(tags=['block-comment'])
class CommentCreateAPIView(CreateAPIView):
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


@extend_schema(tags=['block-comment'])
class CommentDestroyAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'pk'


# ==================================================================Like
@extend_schema(tags=['blog-like'])
class LikeGenericAPIView(GenericAPIView):
    serializer_class = LikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.blog_data
        blog.likes.add(request.user)
        return Response({'message': 'like bosildi'}, status=HTTPStatus.OK)


@extend_schema(tags=['blog-like'])
class LikeCountDestroyAPIView(GenericAPIView):
    serializer_class = LikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.blog_data
        quantity = blog.likes.count()
        return Response({'count': quantity}, status=HTTPStatus.OK)


@extend_schema(tags=['blog-like'])
class LikeRemoveAPIView(GenericAPIView):
    serializer_class = LikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.blog_data
        blog.likes.add(request.user)
        return Response({'message': 'like olibtashlandi'}, status=HTTPStatus.NO_CONTENT)


# ==================================================================Votes
class QuestionVoteGenericAPIView(GenericAPIView):
    serializer_class = VotesSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        question_id = serializer.data
        question = Question.objects.filter(pk=question_id).first()
        question.votes.add(request.user)
        return Response({'message': 'question voted'}, status=HTTPStatus.OK)


@extend_schema(tags=['answer-comment'])
class AnswerCommentCreateAPIView(CreateAPIView):
    serializer_class = AnswerCommentModelSerializer
    queryset = AnswerComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(tags=['answer-comment'])
class AnswerCommentListAPIView(ListAPIView):
    serializer_class = AnswerCommentModelSerializer
    queryset = AnswerComment.objects.all()


@extend_schema(tags=['answer-comment'])
class AnswerCommentDeleteAPIView(DestroyAPIView):
    serializer_class = AnswerCommentModelSerializer
    queryset = AnswerComment.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['answer-comment'])
class AnswerCommentUpdateAPIView(UpdateAPIView):
    serializer_class = AnswerCommentModelSerializer
    queryset = AnswerComment.objects.all()
    lookup_field = 'pk'

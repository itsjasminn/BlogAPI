from http import HTTPStatus

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, \
    GenericAPIView
from rest_framework.response import Response

from apps.models import Answer, AnswerComment
from apps.models import Blog, BlogImages, Comment, Question
from apps.serializers import BlogModelSerializer, BlogImagesModelSerializer, CommentModelSerializer, LikeSerializer, \
    QuestionVotesSerializer, AnswerVotesSerializer
from apps.serializers import QuestionModelSerializer, AnswerModelSerializer, AnswerCommentModelSerializer


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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_authenticated:
            BlogView.objects.get_or_create(blog=instance, user=request.user)

        serializer = self.get_serializer(instance)
        data = serializer.data
        data['views'] = instance.blog_views.count()
        return Response(data)


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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_authenticated:
            QuestionView.objects.get_or_create(question=instance, user=request.user)

        serializer = self.get_serializer(instance)
        data = serializer.data
        data['views'] = instance.question_views.count()
        return Response(data)


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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_authenticated:
            AnswerView.objects.get_or_create(answer=instance, user=request.user)

        serializer = self.get_serializer(instance)
        data = serializer.data
        data['views'] = instance.answer_views.count()
        return Response(data)


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
class LikeCountAPIView(GenericAPIView):
    def get(self, request, pk):
        blog = Blog.objects.filter(pk=pk).first()
        quantity = blog.likes.count()
        return Response({'count': quantity}, status=HTTPStatus.OK)


@extend_schema(tags=['blog-like'])
class LikeRemoveAPIView(GenericAPIView):
    serializer_class = LikeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.blog_data
        blog.likes.remove(request.user)
        return Response({'message': 'like olibtashlandi'}, status=HTTPStatus.NO_CONTENT)


# ==================================================================Votes

@extend_schema(tags=['question-vote'])
class QuestionVoteGenericAPIView(GenericAPIView):
    serializer_class = QuestionVotesSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.question_data
        question.votes.add(request.user)
        return Response({'message': 'vote bosildi'}, status=HTTPStatus.OK)


@extend_schema(tags=['question-vote'])
class QuestionVoteCountAPIView(GenericAPIView):
    def get(self, request, pk):
        question = Question.objects.filter(pk=pk).first()
        count = question.votes.count()
        return Response({'count': count}, status=HTTPStatus.OK)


@extend_schema(tags=['question-vote'])
class QuestionVoteRemoveAPIView(GenericAPIView):
    serializer_class = QuestionVotesSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.question_data
        question.votes.remove(request.user)
        return Response({'message': 'vote olindi'}, status=HTTPStatus.OK)


# ==================================================================Upvotes-Downvotes================================
@extend_schema(tags=['answer-vote'], parameters=[
    OpenApiParameter(
        type=str,
        name='votes',
        required=False
    )
])
class AnswerVoteGenericAPIView(GenericAPIView):
    serializer_class = AnswerVotesSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = serializer.answer_data
        votes = request.query_params.get('votes')
        type = None
        if votes == 'upvote':
            answer.upvotes.add(request.user)
            type = 'upvote'
        if votes == 'downvote':
            answer.downvotes.add(request.user)
            type = 'downvote'
        return Response({'message': f'{type} bosildi'}, status=HTTPStatus.OK)


@extend_schema(tags=['question-vote'], parameters=[
    OpenApiParameter(
        type=str,
        name='votes',
        required=False
    ),
])
class AnswerVoteCountAPIView(GenericAPIView):

    def get(self, request, pk):
        answer = Answer.objects.filter(pk=pk).first()
        votes = request.query_params.get('votes')
        type = None
        count = 0
        if votes == 'upvote':
            count = answer.upvotes.count()
            type = 'upvote'
        if votes == 'downvote':
            count = answer.downvotes.count()
            type = 'downvote'
        return Response({'message': f'{type} soni{count}'}, status=HTTPStatus.OK)


@extend_schema(tags=['answer-vote'], parameters=[
    OpenApiParameter(
        type=str,
        name='votes',
        required=False
    ),
])
@extend_schema(tags=['answer-vote'])
class AnswerVoteRemoveAPIView(GenericAPIView):
    serializer_class = AnswerVotesSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = serializer.answer_data
        votes = request.query_params.get('votes')
        type = None
        if votes == 'upvote':
            answer.upvotes.remove(request.user)
            type = 'upvote'
        if votes == 'downvote':
            answer.downvotes.remove(request.user)
            type = 'downvote'
        return Response({'message': f'{type} olindi'}, status=HTTPStatus.OK)


@extend_schema(tags=['statistics'])
class StatisticsAPIView(ListAPIView):



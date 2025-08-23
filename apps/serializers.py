from rest_framework.serializers import ModelSerializer

from apps.models import Blog, BlogImages, Question, Answer
from authentication.serializers import UserModelSerializer


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'tags')
        read_only_fields = ('created_at', 'author')


class BlogImagesModelSerializer(ModelSerializer):
    class Meta:
        model = BlogImages
        fields = ('blog', 'image')


class QuestionModelSerializer(ModelSerializer):
    author = UserModelSerializer(many=False, read_only=True)

    class Meta:
        model = Question
        fields = ('title', 'content', 'author')
        read_only_fields = ('created_at', 'author')


class AnswerModelSerializer(ModelSerializer):
    author = UserModelSerializer(many=False, read_only=True)
    question = QuestionModelSerializer(many=False, read_only=True)

    class Meta:
        model = Answer
        fields = ('content', 'author', 'question')
        read_only_fields = ('created_at', 'author')

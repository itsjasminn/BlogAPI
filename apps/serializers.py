from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Blog, BlogImages, Comment
from apps.models import Question, Answer
from authentication.serializers import UserModelSerializer


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'tags')
        read_only_fields = ('id', 'created_at', 'author')


class LikeSerializer(Serializer):
    blog = IntegerField(required=True)

    def validate_blog(self, value):
        blog = Blog.objects.filter(pk=value).first()
        self.blog_data = blog
        return blog


class BlogImagesModelSerializer(ModelSerializer):
    class Meta:
        model = BlogImages
        fields = ('id', 'blog', 'image')
        read_only_fields = ('id',)


class QuestionModelSerializer(ModelSerializer):
    author = UserModelSerializer(many=False, read_only=True)

    class Meta:
        model = Question
        fields = ('title', 'content', 'author', 'is_edited')
        read_only_fields = ('created_at', 'author', 'is_edited')

    def update(self, instance, validated_data):
        old_content = instance.content
        new_content = validated_data.get('content', old_content)

        if new_content != old_content:
            validated_data['is_edited'] = True

        return super().update(instance, validated_data)


class AnswerModelSerializer(ModelSerializer):
    author = UserModelSerializer(many=False, read_only=True)

    class Meta:
        model = Answer
        fields = ('content', 'author', 'question', 'is_edited')
        read_only_fields = ('created_at', 'author', 'is_edited',)

    def update(self, instance, validated_data):
        old_content = instance.content
        new_content = validated_data.get('content', old_content)

        if new_content != old_content:
            validated_data['is_edited'] = True

        return super().update(instance, validated_data)


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'created_at', 'blog')
        read_only_fields = ('id', 'created_at', 'author')

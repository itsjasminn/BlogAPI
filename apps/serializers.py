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

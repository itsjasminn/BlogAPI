from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import Blog, BlogImages, Comment


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'tags')
        read_only_fields = ('id', 'created_at', 'author')


class BlogImagesModelSerializer(ModelSerializer):
    class Meta:
        model = BlogImages
        fields = ('id', 'blog', 'image')
        read_only_fields = ('id',)

    def validate_image(self, value):
        if value and not value.name.lower().endswith(('.jpg', 'jpeg', 'png')):
            raise ValidationError('Invalid format!')
        return value


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'created_at', 'blog')
        read_only_fields = ('id', 'created_at', 'author')

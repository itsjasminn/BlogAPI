from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Blog, BlogImages, Comment


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'tags')
        read_only_fields = ('id', 'created_at', 'author')


class LikeSerializer(Serializer):
    blog=IntegerField(required=True)


    def validate_blog(self, value):
        blog=Blog.objects.filter(pk=value).first()
        self.blog_data=blog
        return blog



class VotesSerializer(Serializer):
    pk=IntegerField(required=True)


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

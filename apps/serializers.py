from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import Blog, BlogImages


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'tags')
        read_only_fields = ('created_at', 'author')


class BlogImagesModelSerializer(ModelSerializer):
    class Meta:
        model = BlogImages
        fields = ('blog', 'image')

    def validate_image(self, value):
        if value and not value.name.lower().endswith(('.jpg', 'jpeg', 'png')):
            raise ValidationError('Invalid format!')
        return value

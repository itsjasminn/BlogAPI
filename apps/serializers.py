from rest_framework.serializers import ModelSerializer

from apps.models import Blog


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('author', 'title', 'content', 'tags')
        read_only_fields = ('created_at',)

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from authentication.models import Follow


class FollowingModelSerializer(ModelSerializer):
    class Meta:
        model = Follow
        fields = ('following', 'follower', 'created_at')
        read_only_fields = ('created_at', 'follower')

    def validate_following(self, value):
        user = self.context['request'].user
        if user == value:
            raise ValidationError("Siz ozingizga ozingiz obuna bololmaysiz")
        return value

from http import HTTPStatus

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, \
    GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import User, Follow, Topic
from authentication.serializers import UserModelSerializer, UserUpdateSerializer, ChangePasswordSerializer, \
    FollowingModelSerializer, TopicModelSerializer, FollowTopicSerializer


@extend_schema(tags=['auth'])
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['auth'])
class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer
    lookup_field = 'pk'


@extend_schema(tags=['auth'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer


@extend_schema(tags=['auth'])
class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'


@extend_schema(tags=['auth'])
class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer


@extend_schema(tags=['passwd'])
class ChangePasswordAPIView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer


@extend_schema(tags=['follow'])
class FollowingCreateAPIView(CreateAPIView):
    serializer_class = FollowingModelSerializer

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


@extend_schema(tags=['follow'], parameters=[
    OpenApiParameter(
        name='follower',
        description='enter follower',
        required=False,
        type=str,
    ),
    OpenApiParameter(
        name='following',
        description='enter follower',
        required=False,
        type=str,
    )])
class FollowsListAPiView(ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowingModelSerializer

    def get_queryset(self):
        query = super().get_queryset()
        follower = self.request.query_params.get('follower')
        following = self.request.query_params.get('following')
        if follower:
            query = query.filter(follower=self.request.user)
        if following:
            query = query.filter(following=self.request.user)
        return query


@extend_schema(tags=['topics'])
class TopicCreateAPIView(CreateAPIView):
    serializer_class = TopicModelSerializer


@extend_schema(tags=['topics'])
class TopicListApiView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicModelSerializer

@extend_schema(tags=['follow_toppics'])
class FollowTopicGenericAPIView(GenericAPIView):
    serializer_class = FollowTopicSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        topic_id = serializer.validated_data.get('topic_id')
        request.user.topic_followed.add(topic_id)
        return Response({'message': 'Topic saved'}, status=HTTPStatus.OK)



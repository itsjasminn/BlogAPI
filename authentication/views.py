import random
from http import HTTPStatus

from drf_spectacular.utils import extend_schema, OpenApiParameter
from orjson import orjson
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authentication.models import User, Follow
from authentication.serializers import FollowingModelSerializer, VerifyCodeSerializer
from authentication.serializers import UserModelSerializer, UserUpdateSerializer, ChangePasswordSerializer
from authentication.tasks import send_code_email
from root.settings import redis


@extend_schema(tags=['auth'])
class UserGenericAPIView(GenericAPIView):
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        code = str(random.randrange(10 ** 5, 10 ** 6))
        send_code_email.delay(user, code)
        redis.set(code, orjson.dumps(user))
        return Response({'message': 'Tastiqlash kodi jonatilid'}, status=HTTPStatus.OK)


@extend_schema(tags=['auth'])
class VerifyCodeGenericAPIView(GenericAPIView):
    serializer_class = VerifyCodeSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.context.get('user_data')
        user = User.objects.create(**user_data)
        return Response(UserModelSerializer(user).data, status=HTTPStatus.CREATED)


@extend_schema(tags=['auth'])
class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'pk'


@extend_schema(tags=['auth'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username', 'first_name', 'last_name']


@extend_schema(tags=['auth'])
class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'pk'


@extend_schema(tags=['auth'])
class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['passwd'])
class ChangePasswordAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


# ============================================ Follower ==================================

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


@extend_schema(tags=['follow'])
class FollowDestroyAPIView(DestroyAPIView):
    queryset = Follow.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        follow_id = self.kwargs.get(self.lookup_field)
        obj = Follow.objects.filter(following=follow_id).first()
        if not obj:
            raise NotFound("Follow topilmadi yoki sizga tegishli emas")
        return obj

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response({'message': 'Muvofaqiyatli ochirildi'}, status=HTTPStatus.NO_CONTENT)

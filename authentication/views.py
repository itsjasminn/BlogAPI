from http import HTTPStatus

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, \
    GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from authentication.models import Follow, Topic
from authentication.models import User
from authentication.serializers import FollowingModelSerializer, TopicModelSerializer, FollowTopicSerializer
from authentication.serializers import UserModelSerializer, UserUpdateSerializer, ChangePasswordSerializer


@extend_schema(tags=['auth'])
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]


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


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authentication.serializers import SendVerificationSerializer, VerifyCodeSerializer
from authentication.services import OtpService
from authentication.utils import generate_code
from authentication.models import User

otp_service = OtpService()


class SendOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SendVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = generate_code()

        success, ttl = otp_service.set_code_email(email, str(code))
        if not success:
            return Response(
                {"detail": f"Please wait {ttl} seconds before requesting another code."},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        return Response({"detail": "Verification code sent."}, status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        verified, user_data = otp_service.verify_email(email, code)
        if verified:
            if user_data:
                user = User.objects.create_user(**user_data)
                return Response({"detail": "User registered successfully!"}, status=status.HTTP_201_CREATED)

            return Response({"detail": "Email verified successfully!"}, status=status.HTTP_200_OK)

        return Response({"detail": "Invalid or expired code."}, status=status.HTTP_400_BAD_REQUEST)


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

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView, UserRetrieveAPIView, \
    SendOTPView, VerifyOTPView, TopicCreateAPIView, TopicListApiView, \
    FollowTopicGenericAPIView
from authentication.views import UserListAPIView, ChangePasswordAPIView, FollowingCreateAPIView, FollowsListAPiView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', UserListAPIView.as_view()),
    path('user-create', UserCreateAPIView.as_view()),
    path('user-update/<int:pk>', UserUpdateAPIView.as_view()),
    path('user-delete/<int:pk>', UserDeleteAPIView.as_view()),
    path('user-detail/<int:pk>', UserRetrieveAPIView.as_view()),
    path('user-change-password/<int:pk>', ChangePasswordAPIView.as_view()),

    # OTP
    path('auth/send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('auth/verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
]

urlpatterns += [
    path('following/', FollowingCreateAPIView.as_view()),
    path('follows/list/', FollowsListAPiView.as_view()),
    path('topics/create/', TopicCreateAPIView.as_view()),
    path('topics/list/', TopicListApiView.as_view()),
    path('follow/topic/', FollowTopicGenericAPIView.as_view()),
]

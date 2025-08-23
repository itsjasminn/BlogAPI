from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserGenericAPIView, UserUpdateAPIView, UserDeleteAPIView, FollowDestroyAPIView
from authentication.views import UserListAPIView, ChangePasswordAPIView, FollowingCreateAPIView, FollowsListAPiView
from authentication.views import VerifyCodeGenericAPIView, UserRetrieveAPIView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', UserListAPIView.as_view()),
    path('user-create', UserGenericAPIView.as_view()),
    path('user-update/<int:pk>', UserUpdateAPIView.as_view()),
    path('user-delete/<int:pk>', UserDeleteAPIView.as_view()),
    path('user-detail/<int:pk>', UserRetrieveAPIView.as_view()),
    path('user-change-password/<int:pk>', ChangePasswordAPIView.as_view()),
    path('verify/code', VerifyCodeGenericAPIView.as_view()),
]

urlpatterns += [
    path('following/', FollowingCreateAPIView.as_view()),
    path('follows/list/', FollowsListAPiView.as_view()),
    path('following/delete/<int:pk>', FollowDestroyAPIView.as_view()),
]

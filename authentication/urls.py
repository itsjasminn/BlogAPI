from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView, UserRetrieveAPIView, \
    UserListAPIView, ChangePasswordAPIView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-create', UserCreateAPIView.as_view()),
    path('user-update/<int:pk>', UserUpdateAPIView.as_view()),
    path('user-delete/<int:pk>', UserDeleteAPIView.as_view()),
    path('user-detail/<int:pk>', UserRetrieveAPIView.as_view()),
    path('users', UserListAPIView.as_view()),
    path('user-change-password/<int:pk>', ChangePasswordAPIView.as_view()),
]

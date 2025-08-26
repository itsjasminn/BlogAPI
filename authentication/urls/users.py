from django.urls import path

from authentication.views import *

urlpatterns = [
    path('user-create', UserGenericAPIView.as_view()),
    path('user-update/<int:pk>', UserUpdateAPIView.as_view()),
    path('user-delete/<int:pk>', UserDeleteAPIView.as_view()),
    path('user-detail/<int:pk>', UserRetrieveAPIView.as_view()),
    path('user-change-password/<int:pk>', ChangePasswordAPIView.as_view()),
    path('verify/code', VerifyCodeGenericAPIView.as_view()),
]

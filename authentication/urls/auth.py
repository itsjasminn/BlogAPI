from django.urls import path

from authentication.views import *

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserGenericAPIView.as_view()),
]

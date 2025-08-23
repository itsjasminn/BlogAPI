from django.urls import path

from apps.views import BlogCreateAPIView, BlogListAPIView, BlogDestroyAPIView, BlogUpdateAPIView, BlogDetailAPIView

url_patterns = [
    path('blog-create', BlogCreateAPIView.as_view()),
    path('blogs', BlogListAPIView.as_view()),
    path('blog-delete/<int:pk>', BlogDestroyAPIView.as_view()),
    path('blog-update/<int:pk>', BlogUpdateAPIView.as_view()),
    path('blog-detail/<int:pk>', BlogDetailAPIView.as_view()),

]

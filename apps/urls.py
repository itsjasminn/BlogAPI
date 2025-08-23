from django.urls import path

from apps.views import BlogCreateAPIView, BlogListAPIView, BlogDestroyAPIView, BlogUpdateAPIView, BlogDetailAPIView, \
    BlogImagesDetailAPIView, BlogImagesUpdateAPIView, BlogImagesDestroyAPIView, BlogImagesCreateAPIView, \
    BlogImagesListAPIView, CommentCreatAPIView, CommentListAPIView

urlpatterns = [
    path('blog-create', BlogCreateAPIView.as_view()),
    path('blogs', BlogListAPIView.as_view()),
    path('blog-delete/<int:pk>', BlogDestroyAPIView.as_view()),
    path('blog-update/<int:pk>', BlogUpdateAPIView.as_view()),
    path('blog-detail/<int:pk>', BlogDetailAPIView.as_view()),
    path('blog-images-create', BlogImagesCreateAPIView.as_view()),
    path('blogs', BlogImagesListAPIView.as_view()),
    path('blog-images-detail/<int:pk>', BlogImagesDetailAPIView.as_view()),
    path('blog-images-update/<int:pk>', BlogImagesUpdateAPIView.as_view()),
    path('blog-images-delete/<int:pk>', BlogImagesDestroyAPIView.as_view()),

]

urlpatterns += [
    path('commnet', CommentCreatAPIView.as_view()),
    path('commnet/list/<int:pk>', CommentListAPIView.as_view())
]

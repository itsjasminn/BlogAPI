from django.urls import path

from apps.views import BlogCreateAPIView, BlogListAPIView, LikeCountDestroyAPIView, BlogUpdateAPIView, \
    BlogDetailAPIView, \
    CommentDestroyAPIView, QuestionVoteGenericAPIView
from apps.views import BlogImagesCreateAPIView
from apps.views import BlogImagesDetailAPIView, BlogImagesUpdateAPIView, BlogImagesDestroyAPIView
from apps.views import BlogImagesListAPIView, CommentCreatAPIView, CommentListAPIView, LikeGenericAPIView

urlpatterns = [
    path('blog-create', BlogCreateAPIView.as_view()),
    path('blogs', BlogListAPIView.as_view()),
    path('blog-delete/<int:pk>', LikeCountDestroyAPIView.as_view()),
    path('blog-update/<int:pk>', BlogUpdateAPIView.as_view()),
    path('blog-detail/<int:pk>', BlogDetailAPIView.as_view()),
    path('blog-images-create', BlogImagesCreateAPIView.as_view()),
    path('blogs', BlogImagesListAPIView.as_view()),
    path('blog-images-detail/<int:pk>', BlogImagesDetailAPIView.as_view()),
    path('blog-images-update/<int:pk>', BlogImagesUpdateAPIView.as_view()),
    path('blog-images-delete/<int:pk>', BlogImagesDestroyAPIView.as_view()),
    path('block/like', LikeGenericAPIView.as_view()),

]

urlpatterns += [
    path('commnet', CommentCreatAPIView.as_view()),
    path('commnet/list/<int:pk>', CommentListAPIView.as_view()),
    path('commnet/delete/<int:pk>', CommentDestroyAPIView.as_view()),
]



urlpatterns += [
    path('question/votes',QuestionVoteGenericAPIView.as_view())
]
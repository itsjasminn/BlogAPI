from django.urls import path

from apps.views import BlogCreateAPIView, BlogListAPIView, BlogDestroyAPIView, BlogUpdateAPIView, BlogDetailAPIView, \
    BlogImagesDetailAPIView, BlogImagesUpdateAPIView, BlogImagesDestroyAPIView, BlogImagesCreateAPIView, \
    BlogImagesListAPIView, QuestionCreateAPIView, QuestionListAPIView, QuestionDeleteAPIView, QuestionUpdateAPIView, \
    QuestionDetailAPIView, AnswerCreateAPIView, AnswerListAPIView, AnswerDeleteAPIView, AnswerUpdateAPIView, \
    AnswerDetailAPIView
from apps.views import BlogCreateAPIView, BlogListAPIView, BlogDestroyAPIView, BlogUpdateAPIView, BlogDetailAPIView
from apps.views import BlogImagesCreateAPIView
from apps.views import BlogImagesDetailAPIView, BlogImagesUpdateAPIView, BlogImagesDestroyAPIView
from apps.views import BlogImagesListAPIView, CommentCreatAPIView, CommentListAPIView, BlogLikeGenericAPIView

# blog
urlpatterns = [
    path('blog-create', BlogCreateAPIView.as_view()),
    path('blogs', BlogListAPIView.as_view()),
    path('blog-delete/<int:pk>', BlogDestroyAPIView.as_view()),
    path('blog-update/<int:pk>', BlogUpdateAPIView.as_view()),
    path('blog-detail/<int:pk>', BlogDetailAPIView.as_view()),
]

# blog-images
urlpatterns += [
    path('blog-images-create', BlogImagesCreateAPIView.as_view()),
    path('blogs', BlogImagesListAPIView.as_view()),
    path('blog-images-detail/<int:pk>', BlogImagesDetailAPIView.as_view()),
    path('blog-images-update/<int:pk>', BlogImagesUpdateAPIView.as_view()),
    path('blog-images-delete/<int:pk>', BlogImagesDestroyAPIView.as_view()),
]

# question
urlpatterns += [
    path('question-create', QuestionCreateAPIView.as_view()),
    path('questions', QuestionListAPIView.as_view()),
    path('question-delete/<int:pk>', QuestionDeleteAPIView.as_view()),
    path('question-update/<int:pk>', QuestionUpdateAPIView.as_view()),
    path('question-detail/<int:pk>', QuestionDetailAPIView.as_view()),
]

# answers
urlpatterns += [
    path('answer-create', AnswerCreateAPIView.as_view()),
    path('answers', AnswerListAPIView.as_view()),
    path('answer-delete/<int:pk>', AnswerDeleteAPIView.as_view()),
    path('answer-update/<int:pk>', AnswerUpdateAPIView.as_view()),
    path('answer-detail/<int:pk>', AnswerDetailAPIView.as_view()),
    path('block/like', BlogLikeGenericAPIView.as_view()),

]

# comment
urlpatterns += [
    path('commnet', CommentCreatAPIView.as_view()),
    path('commnet/list/<int:pk>', CommentListAPIView.as_view())
]

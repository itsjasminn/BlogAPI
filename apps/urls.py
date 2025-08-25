from django.urls import path

from apps.views import BlogCreateAPIView, BlogListAPIView, BlogDestroyAPIView, BlogUpdateAPIView, BlogDetailAPIView, \
    AnswerCommentDeleteAPIView, AnswerCommentListAPIView, LikeRemoveAPIView, QuestionVoteCountAPIView, \
    QuestionVoteRemoveAPIView, AnswerVoteGenericAPIView, AnswerVoteCountAPIView, AnswerVoteRemoveAPIView, \
    LikeCountAPIView, CommunityStatsView
from apps.views import BlogImagesCreateAPIView
from apps.views import BlogImagesDetailAPIView, BlogImagesUpdateAPIView, BlogImagesDestroyAPIView
from apps.views import BlogImagesListAPIView, CommentCreateAPIView, CommentListAPIView, LikeGenericAPIView
from apps.views import CommentDestroyAPIView, QuestionVoteGenericAPIView
from apps.views import QuestionCreateAPIView, QuestionListAPIView, QuestionDeleteAPIView, QuestionUpdateAPIView, \
    QuestionDetailAPIView, AnswerCreateAPIView, AnswerListAPIView, AnswerDeleteAPIView, AnswerUpdateAPIView, \
    AnswerDetailAPIView, AnswerCommentUpdateAPIView, AnswerCommentCreateAPIView

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
    path('blog/like', LikeGenericAPIView.as_view()),
    path('blog/like/count/<int:pk>', LikeCountAPIView.as_view()),
    path('blog/like/remove', LikeRemoveAPIView.as_view()),

]

# comment
urlpatterns += [
    path('commnet', CommentCreateAPIView.as_view()),
    path('commnet/list/<int:pk>', CommentListAPIView.as_view()),
    path('commnet/delete/<int:pk>', CommentDestroyAPIView.as_view()),
    path('comment', CommentCreateAPIView.as_view()),
    path('comment/list/<int:pk>', CommentListAPIView.as_view())
]

# answer's comment
urlpatterns += [
    path('answer-comment-create', AnswerCommentCreateAPIView.as_view()),
    path('answer-commnet-update/<int:pk>', AnswerCommentUpdateAPIView.as_view()),
    path('answer-commnet-delete/<int:pk>', AnswerCommentDeleteAPIView.as_view()),
    path('answer-comments', AnswerCommentListAPIView.as_view()),

]

urlpatterns += [
    path('question/votes', QuestionVoteGenericAPIView.as_view()),
    path('question/count/votes/<int:pk>/', QuestionVoteCountAPIView.as_view()),
    path('question/remove/votes', QuestionVoteRemoveAPIView.as_view()),
]

urlpatterns += [
    path('answers/votes', AnswerVoteGenericAPIView.as_view()),
    path('answers/count/votes/<int:pk>/', AnswerVoteCountAPIView.as_view()),
    path('answers.remove/votes', AnswerVoteRemoveAPIView.as_view()),
]

# statistics
urlpatterns += [
    path('community-stats/', CommunityStatsView.as_view(), name='community-stats'),
]

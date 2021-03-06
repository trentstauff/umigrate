from django.urls import path
from .api_views import PollListCreate, PollRetrieveUpdateDestroy, PollCommentListCreate, \
    PollCommentRetrieveUpdateDestroy, OptionListCreate, VoteListCreate, PollLike, PollCommentLike

# Polls url patterns
urlpatterns = [
    path('', PollListCreate.as_view()),
    path('<int:id>', PollRetrieveUpdateDestroy.as_view()),
    path('comments/', PollCommentListCreate.as_view()),
    path('comments/<int:id>', PollCommentRetrieveUpdateDestroy.as_view()),
    path('like', PollLike.as_view()),
    path('comments/like', PollCommentLike.as_view()),
    path('options/', OptionListCreate.as_view()),
    path('options/votes/', VoteListCreate.as_view()),
]

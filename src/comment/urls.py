from django.urls import path
from .views import LikeCommentView, ReplyToCommentView

urlpatterns = [
    path(
        "comments/<int:comment_id>/reply/",
        ReplyToCommentView.as_view(),
        name="reply-comment",
    ),
    path(
        "comments/<int:comment_id>/like/",
        LikeCommentView.as_view(),
        name="like-comment",
    ),
]

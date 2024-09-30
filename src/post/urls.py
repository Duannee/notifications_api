from django.urls import path
from .views import CreateCommentView, CreateLikeView

urlpatterns = [
    path(
        "posts/<int:post_id>/comments/",
        CreateCommentView.as_view(),
        name="create-comment",
    ),
    path("posts/int:post_id/likes/", CreateLikeView.as_view(), name="like-post"),
]

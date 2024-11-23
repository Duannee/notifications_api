from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from .models import Post
from comment.models import Comment
from comment.serializers import CommentSerializer
from notification.utils import create_notifications
from like.models import Like
from like.serializers import LikeSerializer
from rest_framework.permissions import IsAuthenticated


class CreateCommentView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs["post_id"])
        comment = serializer.save(user=self.request.user, post=post)

        if post.author != self.request.user:
            create_notifications(
                user=post.author,
                notification_type="comment_post",
                title="New comment on your post ",
                message=f"{self.request.user.username} commented: {comment.content}",
            )


class CreateLikeView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        post = Post.objects.get(self.kwarg["post_id"])
        like = serializer.save(user=self.request.user, post=post)

        if post.author != self.request.user:
            create_notifications(
                user=post.author,
                notification_type="like_post",
                title="Your post received a like ",
                message=f"{self.request.user.username} liked your post",
            )

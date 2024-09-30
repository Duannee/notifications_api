from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from .models import Post
from comment.models import Comment
from comment.serializers import CommentSerializer
from notification.utils import create_notifications


class CreateComment(CreateAPIView):
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

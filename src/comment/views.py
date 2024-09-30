from rest_framework.generics import CreateAPIView
from .models import Comment
from .serializers import CommentSerializer
from post.models import Post
from notification.utils import create_notifications


class ReplyToCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        parent_comment = Comment.objects.get(id=self.kwargs["comment_id"])
        reply = serializer.save(
            user=self.request.user, post=parent_comment.post, parent=parent_comment
        )

        if parent_comment.user != self.request.user:
            create_notifications(
                user=parent_comment.user,
                notification_type="reply_comment",
                title="Reply to your comment",
                message=f"{self.request.user.username} reply: {reply.content}",
            )

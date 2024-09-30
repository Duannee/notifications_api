from rest_framework.generics import CreateAPIView
from .models import Comment
from .serializers import CommentSerializer
from like.models import Like
from like.serializers import LikeSerializer
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


class LikeCommentView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        comment = Comment.objects.get(id=self.kwargs["comment_id"])
        like = serializer.save(user=self.request.user, comment=comment)

        if comment.user != self.request.user:
            create_notifications(
                user=comment.user,
                notification_type="like_comment",
                title="Your comment received a like",
                message=f"{self.request.user.username} liked your comment",
            )

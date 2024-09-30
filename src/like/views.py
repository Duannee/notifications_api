from rest_framework.generics import CreateAPIView
from .models import Like
from .serializers import LikeSerializer
from post.models import Post
from notification.utils import create_notifications


class CreateLike(CreateAPIView):
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

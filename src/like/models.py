from django.db import models
from django.contrib.auth.models import User
from post.models import Posts
from comment.models import Comments


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(
        Posts, null=True, blank=True, on_delete=models.CASCADE, related_name="likes"
    )
    comment = models.ForeignKey(
        Comments, null=True, blank=True, on_delete=models.CASCADE, related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        target = self.post if self.post else self.comment

        return f"Like by {self.user.username} on {target}"

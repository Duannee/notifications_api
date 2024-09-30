from django.db import models
from django.contrib.auth.models import User
from post.models import Posts


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment by {self.user.username} on {self.post}"

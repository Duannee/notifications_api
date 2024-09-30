from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Post by {self.author.username}"

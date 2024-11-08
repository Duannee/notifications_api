from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):

    NOTIFICATION_TYPE_CHOICES = [
        ("comment_post", "Comment on Post"),
        ("reply_comment", "Reply to Comment"),
        ("like_post", "Like on Post"),
        ("like_comment", "Like on Comment"),
        ("new_course", "New Course Available"),
        ("course_update", "Course Updated"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    notification_type = models.CharField(
        max_length=50, choices=NOTIFICATION_TYPE_CHOICES
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    course_id = models.IntegerField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

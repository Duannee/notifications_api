from django.db import models
from django.contrib.auth.models import User


class Notifications(models.Model):
    INTERACTION = "interaction"
    COURSE = "course"
    EVENT = "event"
    ROLE_BASED = "role_based"

    NOTIFICATION_TYPE_CHOICES = [
        (INTERACTION, "Interaction with content"),
        (COURSE, "Course and Classes"),
        (EVENT, "Event"),
        (ROLE_BASED, "Specific role"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    notification_type = models.CharField(
        max_length=50, choices=NOTIFICATION_TYPE_CHOICES
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    post_id = models.IntegerField(null=True, blank=True)
    comment_id = models.IntegerField(null=True, blank=True)
    video_id = models.IntegerField(null=True, blank=True)

    course_id = models.IntegerField(null=True, blank=True)
    update_type = models.CharField(max_length=50, null=True, blank=True)

    event_id = models.IntegerField(null=True, blank=True)
    reminder_time = models.DateTimeField(null=True, blank=True)

    role = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.notification_type} - {self.user.username}"

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course
from notification.models import Notification
from django.contrib.auth.models import User


@receiver(post_save, sender=Course)
def notify_course_events(sender, instance, created, **kwargs):
    users = User.objects.filter(is_superuser=False)
    notification_type = "new_course" if created else "course_update"
    title = f"{"New course" if created else "Updated course"}: {instance.name}"
    message = (
        f"The course {instance.name} {"is available" if created else "was updated"}"
    )

    for user in users:
        Notification.objects.create(
            user=user,
            notification_type=notification_type,
            title=title,
            message=message,
            course_id=instance.id,
        )

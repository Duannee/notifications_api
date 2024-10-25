from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course
from notification.models import Notification


@receiver(post_save, sender=Course)
def notify_course_events(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            use=instance.owner,
            notification_type="new_course",
            title=f"New course: {instance.name}",
            message=f"The course {instance.name} is available",
            course_id=instance.id,
        )
    else:
        Notification.objects.create(
            use=instance.owner,
            notification_type="course_update",
            title=f"Update: {instance.name}",
            message=f"The course {instance.name} was updated",
            course_id=instance.id,
        )

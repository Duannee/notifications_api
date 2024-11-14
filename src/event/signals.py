from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event
from notification.models import Notification
from django.contrib.auth.models import User


@receiver(post_save, sender=Event)
def notify_events(sender, instance, created, **kwargs):
    users = User.objects.filter(is_superuser=False)
    notification_type = "event_created" if created else "event_updated"
    title = f"{"New event" if created else "Update event"}: {instance.title}"
    message = (
        f"The event {instance.title} {"was created" if created else "Was updated"}"
    )

    for user in users:
        Notification.objects.create(
            user=user,
            notification_type=notification_type,
            title=title,
            message=message,
            event_id=instance.id,
        )

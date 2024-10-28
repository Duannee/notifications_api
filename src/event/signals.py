from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event
from notification.models import Notification
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=Event)
def event_notification(sender, instance, created, **kwargs):
    message = (
        f"New event: {instance.title}"
        if created
        else f"Updated event: {instance.title}"
    )
    Notification.objects.create(title="Event", message=message, user=instance.organizer)

    channel_layer = get_channel_layer()
    group_name = f"notifications_{instance.organizer.id}"
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "send_notification",
            "notification": {
                "title": "Event",
                "message": message,
                "timestamp": str(instance.updated_at),
            },
        },
    )

    for participant in instance.participants.all():
        Notification.objects.create(
            title="Event",
            message=f"New event created: {instance.title}",
            user=participant,
        )
        participant_group = f"notifications_{participant.id}"
        async_to_sync(channel_layer.group_send)(
            participant_group,
            {
                "type": "send_notification",
                "notification": {
                    "title": "Event",
                    "message": f"The Event {instance.title} was created",
                    "timestamp": str(instance.updated_at),
                },
            },
        )

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification
from serializers import NotificationSerializer


def create_notifications(user, notification_type, message, title):
    notification = Notification.objects.create(
        user=user, notification_type=notification_type, message=message, title=title
    )

    send_notifications_to_user(notification)


def send_notifications_to_user(notification):
    channels_layer = get_channel_layer()
    user_group = f"notifications_{notification.user.id}"
    notification_data = NotificationSerializer(notification).data

    async_to_sync(channels_layer.group_send)(
        user_group, {"type": "send_notification", "notification": notification_data}
    )

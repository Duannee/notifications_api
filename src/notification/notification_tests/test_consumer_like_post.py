from channels.testing import WebsocketCommunicator
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from core.asgi import application
from asgiref.sync import sync_to_async

User = get_user_model()


class NotificationConsumerTestCase(TestCase):
    """Test to verify the notification consumer with notification type like on post"""

    async def test_notification_consumer_like_post(self):

        user = await sync_to_async(User.objects.create_user)(
            username="testuser", password="12345"
        )

        token = str(AccessToken.for_user(user))

        communicator = WebsocketCommunicator(
            application, f"/ws/notifications/?token={token}"
        )

        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        await communicator.send_json_to(
            {
                "notification_type": "like_post",
                "content": "Somebody liked your post!",
            }
        )

        response = await communicator.receive_json_from()
        self.assertEqual(response["notification_type"], "like_post")
        self.assertEqual(
            response["message"], "New like on your post: Somebody liked your post!"
        )

        await communicator.disconnect()

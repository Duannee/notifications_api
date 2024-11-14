from django.test import TestCase
from rest_framework.test import APIClient
from notification.models import Notification
from event.models import Event
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class EventNotificationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client = APIClient()

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        self.event_data = {
            "title": "title test",
            "description": "description test",
            "organizer": self.user,
        }

    def test_event_create_notification(self):
        """Test to verify if notification is create when the event is create"""

        event = Event.objects.create(**self.event_data)

        notification = Notification.objects.filter(
            user=self.user, notification_type="event_created", event_id=event.id
        ).first()

        self.assertIsNotNone(notification)
        self.assertEqual(notification.title, f"New event: {event.title}")
        self.assertEqual(notification.message, f"The event {event.title} was created")

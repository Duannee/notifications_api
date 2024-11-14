from django.test import TestCase
from rest_framework.test import APIClient
from notification.models import Notification
from course.models import Course
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
            "name": "title test",
            "description": "description test",
            "user": self.user,
        }

    def test_course_update_notification(self):
        """Test to verify if notification is created when the course is updated"""

        course = Course.objects.create(**self.event_data)

        course.name = "Updated Course Name"
        course.save()

        notification = Notification.objects.filter(
            user=self.user, notification_type="course_update", course_id=course.id
        ).first()

        self.assertIsNotNone(notification)
        self.assertEqual(notification.title, f"Updated course: {course.name}")
        self.assertEqual(notification.message, f"The course {course.name} was updated")
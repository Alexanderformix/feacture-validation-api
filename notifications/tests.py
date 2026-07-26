from django.test import TestCase
from notifications.models import Notification


class NotificationTest(TestCase):

    def test_notification_default(self):

        notification = Notification(message="Hola")

        self.assertFalse(notification.read)

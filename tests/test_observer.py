# tests/test_observer.py

import unittest
from notification_system.core.observer import Publisher, NotificationSubscriber

class TestObserver(unittest.TestCase):
    def test_notify_subscribers(self):
        publisher = Publisher()
        sub1 = NotificationSubscriber("User1")
        sub2 = NotificationSubscriber("User2")

        publisher.subscribe(sub1)
        publisher.subscribe(sub2)

        messages = publisher.notify_subscribers("New Notification!")
        self.assertIn("User1 received: New Notification!", messages)
        self.assertIn("User2 received: New Notification!", messages)

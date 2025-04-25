# tests/test_services.py

import unittest
from notification_system.core.services import NotificationServiceFactory

class TestFactory(unittest.TestCase):
    def test_email_service(self):
        service = NotificationServiceFactory.get_service("email")
        self.assertEqual(service.notify("Hi"), "Email: Hi")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            NotificationServiceFactory.get_service("fax")

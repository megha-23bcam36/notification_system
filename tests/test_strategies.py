# tests/test_strategies.py

import unittest
from notification_system.core.strategies import EmailStrategy, SMSStrategy, NotificationContext

class TestStrategy(unittest.TestCase):
    def test_email_strategy(self):
        context = NotificationContext(EmailStrategy())
        self.assertEqual(context.execute_strategy("Hello"), "Email strategy: Hello")

    def test_sms_strategy(self):
        context = NotificationContext(SMSStrategy())
        self.assertEqual(context.execute_strategy("Hello"), "SMS strategy: Hello")

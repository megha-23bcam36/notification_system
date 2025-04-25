# core/strategies.py

class NotificationStrategy:
    def send(self, message):
        raise NotImplementedError

class EmailStrategy(NotificationStrategy):
    def send(self, message):
        return f"Email strategy: {message}"

class SMSStrategy(NotificationStrategy):
    def send(self, message):
        return f"SMS strategy: {message}"

class NotificationContext:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def execute_strategy(self, message):
        return self.strategy.send(message)

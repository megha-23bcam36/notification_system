# core/observer.py

class Subscriber:
    def update(self, message):
        raise NotImplementedError

class NotificationSubscriber(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        return f"{self.name} received: {message}"

class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, message):
        return [subscriber.update(message) for subscriber in self.subscribers]

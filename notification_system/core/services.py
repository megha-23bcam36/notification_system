# core/services.py

class EmailService:
    def notify(self, message):
        return f"Email: {message}"

class SMSService:
    def notify(self, message):
        return f"SMS: {message}"

class NotificationServiceFactory:
    @staticmethod
    def get_service(service_type):
        if service_type == "email":
            return EmailService()
        elif service_type == "sms":
            return SMSService()
        else:
            raise ValueError("Invalid service type")

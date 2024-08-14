from abc import ABC
from dataclasses import dataclass
from enum import Enum

# COMPLETE THIS CLASS
@dataclass
class Notification(ABC):
    def __init__(self,recipient: str, message: str,sender:str):
        self.recipient = recipient
        self.message = message
        self.sender = sender

    def send_notification(self):
        pass
    def notification_type(self):
        pass

class NotificationType(Enum):
    EMAIL = "Email"
    PUSH = "Push"
    SMS = "SMS"

@dataclass
class EmailNotification(Notification):
    def __init__(self, recipient, message,sender, *args):
        super().__init__(recipient, message,sender)


    def send_notification(self):
        print(f"Email sent to {self.recipient} from {self.sender}")
        print(f"Message: {self.message}")

    def notification_type(self):
        return NotificationType.EMAIL


@dataclass
class PushNotification(Notification):
    def __init__(self, recipient, message,*args :str):
        super().__init__(recipient, message,*args)


    def send_notification(self):
        print(f"Push notification sent to device {self.recipient}")
        print(f"Message: {self.message}")

    def notification_type(self):
        return NotificationType.PUSH


@dataclass
class SmsNotification(Notification):
    def __init__(self, recipient, message,*args):
        super().__init__(recipient, message, *args)

    def send_notification(self):
        print(f"SMS sent to {self.recipient}")
        print(f"Message: {self.message}")

    def notification_type(self):
        return NotificationType.SMS

from .products import Notification,NotificationType,EmailNotification,PushNotification,SmsNotification


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type: NotificationType, *args):
        if notification_type == NotificationType.EMAIL:
            # recipient, message, sender = args
            return EmailNotification(*args)
        elif notification_type == NotificationType.SMS:
            # recipient, message = args
            return SmsNotification(*args)
        elif notification_type == NotificationType.PUSH:
            # recipient, message = args
            return PushNotification(*args)
        else:
            raise ValueError(f"Unknown notification type {notification_type}")

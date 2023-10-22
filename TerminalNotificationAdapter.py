from NotificationAdapter import NotificationAdapter

class TerminalNotificationAdapter(NotificationAdapter):
    def send_notification(self, message):
        print(f"Terminal Notification: {message}")

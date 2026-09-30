class Notification:
    def __init__(self, recipient):
        self.recipient = recipient
    def send(self):
        print("Sending Notification")
class EmailNotification(Notification):
    def send(self):
        print(f"Sending Email to {self.recipient}")
class SMSNotification(Notification):
    def send(self):
        print(f"Sending SMS to {self.recipient}")
email = EmailNotification("user@example.com")
sms = SMSNotification("0812345678")

notifications = [email, sms]
for notification in notifications:
    notification.send()
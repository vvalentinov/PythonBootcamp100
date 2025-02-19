import smtplib

from twilio.rest import Client


class NotificationManager:

    def __init__(self, twilio_sid: str, twilio_token: str):
        self.client = Client(twilio_sid, twilio_token)

    def send_sms(self, message_body: str, from_number: str, to_number: str):
        message = self.client.messages.create(
            from_=from_number,
            body=message_body,
            to=to_number
        )

        print(message.sid)

    @staticmethod
    def send_emails(email_list, email_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="sender_email...", password="app_password...")
            for email in email_list:
                connection.sendmail(
                    from_addr="sender_email...",
                    to_addrs=email,
                    msg=f"Subject:Low Price Flight!\n\n{email_body}".encode('utf-8'))

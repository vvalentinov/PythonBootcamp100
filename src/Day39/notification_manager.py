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


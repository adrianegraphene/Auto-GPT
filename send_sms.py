import os
from twilio.rest import Client


class TwilioClient:
    FROM_NUMBER = os.environ["FROM_PHONE_NUMBER"]

    def __init__(self):
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.client = Client(account_sid, auth_token)

    # Use this method to send a single text to a phone number at +___________
    def send_sms(self, phone_number, sms):
        from_number = self.FROM_NUMBER
        message = self.client.messages.create(to=phone_number, from_=from_number, body=sms)
        return message.sid
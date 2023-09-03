from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

sender_number = os.getenv("sender_number")
receiver_number = os.getenv("receiver_number")
twilio_account_SID = os.getenv("twilio_SID")
twilio_auth_Token = os.getenv("twilio_Token")


class NotificationManager:
    """
    The NotificationManager class is responsible for sending notifications with flight deal details using the Twilio API.

    Attributes:
    - client (Client): An instance of the Twilio Client class for sending SMS messages.

    Methods:
    - __init__(self) -> None:
        Initializes an instance of the NotificationManager class with Twilio credentials.

    - send_message(self, body: str) -> Message:
        Sends an SMS message with the specified body to the designated recipient.

        Parameters:
        - body (str): The text content of the SMS message.

        Returns:
        - Message: An instance of the Twilio Message class representing the sent message.

    Example Usage:
    notification_manager = NotificationManager()
    notification_manager.send_message("Great flight deal found! Tk450.99 from New York to Los Angeles.")
    """

    def __init__(self):
        """
        Initializes an instance of the NotificationManager class with Twilio credentials.
        """
        self.client = Client(twilio_account_SID, twilio_auth_Token)

    def send_message(self, body: str):
        """
        Sends an SMS message with the specified body to the designated recipient.

        Parameters:
        - body (str): The text content of the SMS message.

        Returns:
        - Message: An instance of the Twilio Message class representing the sent message.
        """
        return self.client.messages \
            .create(
            body=body,
            from_=sender_number,
            to=receiver_number
        )

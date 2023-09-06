# Import required libraries and modules
from twilio.rest import Client  # Twilio library for sending SMS messages
import os  # Operating System library for working with environment variables
from dotenv import load_dotenv  # Library for loading environment variables
import smtplib  # SMTP library for sending email messages
import requests  # Library for making HTTP requests

# Load environment variables from a .env file
load_dotenv()

# Retrieve environment variables for API URLs, phone numbers, and credentials
users_url = os.getenv("users_url")
sender_number = os.getenv("sender_number")
receiver_number = os.getenv("receiver_number")
twilio_account_SID = os.getenv("twilio_SID")
twilio_auth_Token = os.getenv("twilio_Token")
my_email = os.getenv("my_email")
my_pass = os.getenv("my_pass")

# Fetch user data from an external source (assumed to be a URL)
data = requests.get(url=users_url).json()["users"]

# Define the NotificationManager class responsible for sending notifications
class NotificationManager:
    """
    The NotificationManager class is responsible for sending notifications with flight deal
    details using the Twilio API.

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

    - send_mail(self, body):
        Sends an email message with the specified body to multiple recipients.

        Parameters:
        - body (str): The text content of the email message.

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

    def send_mail(self, body):
        """
        Sends an email message with the specified body to multiple recipients.

        Parameters:
        - body (str): The text content of the email message.
        """
        data = requests.get(url=users_url).json()["users"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_pass)
            for x in data:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=x["email"],
                    msg=f"Subject: New Low Price Flight \n\n {body}",
                )



# Import necessary modules and set up date calculations

# Import the DataManager class for managing flight data
from data_manager import DataManager

# Import the FlightSearch class for searching flight deals
from flight_search import FlightSearch

# Import the NotificationManager class for sending notifications
from notification_manager import NotificationManager

# Import the datetime module for working with dates and times
import datetime

# Import the load_dotenv function from the dotenv library for loading environment variables
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Calculate the date for tomorrow and a date 180 days from tomorrow
tomorrow = datetime.datetime.now() + datetime.timedelta(hours=24)
after = tomorrow + datetime.timedelta(days=180)

# Define the IATA code of the origin city (Dhaka, for example)
origin_city_code = "DAC"

# Initialize instances of DataManager, FlightSearch, and NotificationManager

# Initialize an instance of the DataManager class to manage flight data
data_manager = DataManager()

# Get flight data from an external source (e.g., Google Sheets)
sheet_data = data_manager.get_data()

# Initialize an instance of the FlightSearch class for searching flight deals
flight_search = FlightSearch()

# Initialize an instance of the NotificationManager class for sending notifications
notification_manager = NotificationManager()

# Loop through the retrieved flight data

# Iterate over each entry in the flight data
for x in sheet_data:

    # Check if the IATA code is missing for a city
    if x["iataCode"] == "":

        # If the IATA code is missing, update it using FlightSearch
        data_manager.update_data(x)

    # Check for flight deals using FlightSearch

    # Call the check_flight method to search for flight deals
    flight = flight_search.check_flight(
        origin_city_code=origin_city_code,
        destination_city_code=x["iataCode"],
        departure_date=tomorrow,
        comeback_date=after,
    )

    # Skip to the next iteration if no flight deals are found
    if flight is None:
        continue

    # Create a notification message body with flight details

    # Build a message body with flight details
    body = (f"Great deal alert! You can fly from {flight.origin_city}-{flight.origin_airport} to"
            f" {flight.destination_city}-{flight.destination_airport} for only Tk{flight.price}."
            f" Travel dates: {flight.out_date} to {flight.return_date}.")

    # Add information about stopovers if applicable
    if flight.stop_overs > 0:
        body += f" Flight has {flight.stop_overs} stop over, via {flight.via_city}."

    # Send a notification email with flight details and a deep link

    # Call the send_mail method to send a notification email
    notification_manager.send_mail(body=f"{body}\n {flight.link}\n")

    # Send a notification if a low-priced flight is found

    # Uncomment the following lines to send an SMS notification for low-priced flights
    # if flight.price <= x["lowestPrice"]:
    #     notification_manager.send_message(
    #         body=f"Great deal alert! You can fly from "
    #              f"{flight.origin_city}-{flight.origin_airport} to "
    #              f"{flight.destination_city}-{flight.destination_airport} for only Tk{flight.price}. "
    #              f"Travel dates: {flight.out_date} to {flight.return_date}"
    #     )

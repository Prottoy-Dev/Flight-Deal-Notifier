# Import necessary modules and set up date calculations
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime

# Calculate the date for tomorrow and a date 180 days from tomorrow
tomorrow = datetime.datetime.now() + datetime.timedelta(hours=24)
after = tomorrow + datetime.timedelta(days=180)

# Define the IATA code of the origin city (Dhaka, for example)
origin_city_code = "DAC"

# Initialize instances of DataManager, FlightSearch, and NotificationManager
data_manager = DataManager()
sheet_data = data_manager.get_data()  # Get flight data from an external source (e.g., Google Sheets)

flight_search = FlightSearch()
notification_manager = NotificationManager()

# Loop through the retrieved flight data
for x in sheet_data:
    if x["iataCode"] == "":
        # If the IATA code is missing, update it using FlightSearch
        data_manager.update_data(x)

# Loop through the updated flight data
for x in sheet_data:
    # Check for flight deals using FlightSearch
    flight = flight_search.check_flight(
        origin_city_code=origin_city_code,
        destination_city_code=x["iataCode"],
        departure_date=tomorrow,
        comeback_date=after,
    )

    # Send a notification if a low-priced flight is found
    if flight.price <= x["lowestPrice"]:
        notification_manager.send_message(
            body=f"Great deal alert! You can fly from "
                 f"{flight.origin_city}-{flight.origin_airport} to "
                 f"{flight.destination_city}-{flight.destination_airport} for only Tk{flight.price}. "
                 f"Travel dates: {flight.out_date} to {flight.return_date}"
        )
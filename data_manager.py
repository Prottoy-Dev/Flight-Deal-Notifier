import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the URL from environment variables
sheety_get_url = os.getenv("sheety_get_url")

class DataManager:
    """
    The DataManager class manages the retrieval and updating of flight price data using external APIs and data sources.
    """

    def __init__(self):
        """
        Initializes an instance of the DataManager class.

        Attributes:
        - self.data (dict): A dictionary that stores the retrieved flight price data.
        """
        self.data = {}

    def get_data(self):
        """
        Retrieves flight price data from an external data source using an HTTP GET request.

        Returns:
        - self.data (dict): A dictionary containing flight price data.
        """
        self.data = requests.get(url=sheety_get_url).json()["prices"]
        return self.data

    def update_data(self, city):
        """
        Updates the flight price data for a specific city by sending an HTTP PUT request to an external data source.

        Parameters:
        - city (dict): A dictionary containing information about the city to be updated.
            - city["id"] (str): The unique identifier for the city's data in the external data source.

        Dependencies:
        - This method relies on the FlightSearch class from the flight_search module to retrieve updated flight price data.
        """
        from flight_search import FlightSearch
        flight_search = FlightSearch()

        new_data = {
            "price": {
                "iataCode": flight_search.get_data(city["city"])
            }
        }

        # Send an HTTP PUT request to update the data for the specified city
        response = requests.put(url=f"{sheety_get_url}/{city['id']}", json=new_data)

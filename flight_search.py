# Import required libraries and modules
import requests  # Library for making HTTP requests
import os  # Operating System library for working with environment variables
from dotenv import load_dotenv  # Library for loading environment variables
from flight_data import FlightData  # Importing FlightData class from a module

# Load environment variables from a .env file
load_dotenv()

# Retrieve the URLs and API key from environment variables
tequila_search_url = os.getenv("tequila_search_url")
tequila_locations_url = os.getenv("tequila_locations_url")
tequila_key = os.getenv("tequila_key")

# Define the FlightSearch class responsible for interacting with flight search APIs
class FlightSearch:
    """
    The FlightSearch class is responsible for interfacing with flight search APIs to retrieve flight data and perform flight searches.
    """

    def get_data(self, city_name: str) -> str:
        """
        Retrieves the IATA code for a given city using a flight search API.

        Parameters:
        - city_name (str): The name of the city for which the IATA code is to be retrieved.

        Returns:
        - str: The IATA code of the specified city.
        """
        # Define HTTP headers and parameters for the API request
        header = {
            "apikey": tequila_key
        }
        term = {
            "term": city_name
        }

        # Make an HTTP GET request to retrieve city information
        result = requests.get(url=tequila_locations_url, params=term, headers=header).json()

        # Extract and return the IATA code of the city
        self.code = result["locations"][0]["code"]
        return self.code

    def check_flight(self, origin_city_code: str, destination_city_code: str, departure_date,
                     comeback_date) -> FlightData:
        """
        Performs a flight search between two cities with specified departure and return dates.

        Parameters:
        - origin_city_code (str): The IATA code of the origin city.
        - destination_city_code (str): The IATA code of the destination city.
        - departure_date (datetime.date): The departure date of the flight.
        - comeback_date (datetime.date): The return date of the flight.

        Returns:
        - FlightData: An instance of the FlightData class containing information about the flight, including price,
                      origin, destination, and travel dates.
        """
        # Define HTTP headers and parameters for the flight search API request
        header = {
            "apikey": tequila_key
        }
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": departure_date.strftime("%d/%m/%Y"),
            "date_to": comeback_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "one_for_city": 1,
            "curr": "BDT"  # Currency code (assuming it's Bangladeshi Taka)
        }

        # Make an HTTP GET request to perform the flight search
        response = requests.get(url=tequila_search_url, params=parameters, headers=header)

        # Try to extract flight data from the API response
        try:
            data = response.json()["data"][0]
        except IndexError:
            # If no direct flight found, update parameters to allow 1 stopover
            parameters["max_stopovers"] = 1
            response = requests.get(url=tequila_search_url, params=parameters, headers=header)
            try:
                data = response.json()["data"][0]
            except IndexError:
                # If still no flight found, update parameters to allow 2 stopovers
                parameters["max_stopovers"] = 2
                response = requests.get(url=tequila_search_url, params=parameters, headers=header)
                try:
                    data = response.json()["data"][0]
                except IndexError:
                    print(f"No flight with {parameters['max_stopovers']} stop "
                          f"overs from {origin_city_code} to {destination_city_code}")
                    return None
                else:
                    # Create FlightData instance with 2 stopovers
                    flight_data = FlightData(
                        price=data["price"],
                        origin_city=data["cityFrom"],
                        origin_airport=data["cityCodeFrom"],
                        destination_city=data["cityTo"],
                        destination_airport=data["cityCodeTo"],
                        out_date=data["route"][0]["local_departure"].split("T")[0],
                        return_date=data["route"][-1]["local_departure"].split("T")[0],
                        stop_overs=2,
                        link=data["deep_link"],
                        via_city=f"{data['route'][0]['cityTo']} and {data['route'][1]['cityTo']}"
                    )
                    print(f"{flight_data.destination_city}: Tk{flight_data.price}")
                    return flight_data
            else:
                # Create FlightData instance with 1 stopover
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["cityFrom"],
                    origin_airport=data["cityCodeFrom"],
                    destination_city=data["cityTo"],
                    destination_airport=data["cityCodeTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    link=data["deep_link"],
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: Tk{flight_data.price}")
                return flight_data
        else:
            # Create FlightData instance for direct flight
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["cityCodeFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["cityCodeTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                link=data["deep_link"],
            )
            print(f"{flight_data.destination_city}: Tk{flight_data.price}")
            return flight_data

import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData  # Assuming FlightData is imported from a module

load_dotenv()

tequila_search_url = os.getenv("tequila_search_url")
tequila_locations_url = os.getenv("tequila_locations_url")
tequila_key = os.getenv("tequila_key")


class FlightSearch:
    """
    The FlightSearch class is responsible for interfacing with flight search APIs to retrieve flight data and perform flight searches.

    Attributes:
    - None

    Methods:
    - get_data(self, city_name: str) -> str:
        Retrieves the IATA code for a given city using a flight search API.

        Parameters:
        - city_name (str): The name of the city for which the IATA code is to be retrieved.

        Returns:
        - str: The IATA code of the specified city.

    - check_flight(self, origin_city_code: str, destination_city_code: str, departure_date: datetime.date, comeback_date: datetime.date) -> FlightData:
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

    def get_data(self, city_name: str) -> str:
        """
        Retrieves the IATA code for a given city using a flight search API.

        Parameters:
        - city_name (str): The name of the city for which the IATA code is to be retrieved.

        Returns:
        - str: The IATA code of the specified city.
        """
        header = {
            "apikey": tequila_key
        }
        term = {
            "term": city_name
        }
        result = requests.get(url=tequila_locations_url, params=term, headers=header).json()
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
            "one_for_city": 1,
            "curr": "BDT"  # Currency code (assuming it's Bangladeshi Taka)
        }
        response = requests.get(url=tequila_search_url, params=parameters, headers=header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["cityCodeFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["cityCodeTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: Tk{flight_data.price}")
        return flight_data

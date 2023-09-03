class FlightData:
    """
    The FlightData class is responsible for structuring flight data. It stores information about flight prices,
    cities, airports, and travel dates.

    Attributes:
    - price (float): The price of the flight.
    - origin_city (str): The name of the origin city.
    - origin_airport (str): The code or name of the origin airport.
    - destination_city (str): The name of the destination city.
    - destination_airport (str): The code or name of the destination airport.
    - out_date (str): The departure date of the flight in the format "YYYY-MM-DD".
    - return_date (str): The return date of the flight in the format "YYYY-MM-DD".

    Methods:
    - __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        Initializes an instance of the FlightData class with flight details.

    Example Usage:
    flight_info = FlightData(450.99, "New York", "JFK", "Los Angeles", "LAX", "2023-09-15", "2023-09-22")
    """

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                 return_date):
        """
        Initializes an instance of the FlightData class with flight details.

        Parameters:
        - price (float): The price of the flight.
        - origin_city (str): The name of the origin city.
        - origin_airport (str): The code or name of the origin airport.
        - destination_city (str): The name of the destination city.
        - destination_airport (str): The code or name of the destination airport.
        - out_date (str): The departure date of the flight in the format "YYYY-MM-DD".
        - return_date (str): The return date of the flight in the format "YYYY-MM-DD".
        """
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

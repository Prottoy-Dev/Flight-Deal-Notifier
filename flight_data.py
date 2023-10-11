class FlightData:
 
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport,
                 out_date, return_date, link, stop_overs=0, via_city=""):
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
        - stop_overs (int, optional): The number of stopovers or layovers during the flight (default is 0).
        - via_city (str, optional): The name of the city where a layover occurs (default is an empty string).
        - link (str): The URL link to more information about the flight.
        """
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.link = link

class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price


def get_flight_table():
    return [
        {
            "flight_id": "AI161E90",
            "from_city": "BLR",
            "to_city": "BOM",
            "price": 5600,
        },
        {
            "flight_id": "BR161F91",
            "from_city": "BOM",
            "to_city": "BBI",
            "price": 6750,
        },
        {
            "flight_id": "AI161F99",
            "from_city": "BBI",
            "to_city": "BLR",
            "price": 8210,
        },
        {
            "flight_id": "VS171E20",
            "from_city": "JLR",
            "to_city": "BBI",
            "price": 5500,
        },
        {
            "flight_id": "AS171G30",
            "from_city": "HYD",
            "to_city": "JLR",
            "price": 4400,
        },
        {
            "flight_id": "AI131F49",
            "from_city": "HYD",
            "to_city": "BOM",
            "price": 3499,
        },
    ]


def search_flights(flight_table, search_criteria):
    if search_criteria == 1:
        
        city = input("Enter the city: ")
        filtered_flights = [
            flight for flight in flight_table if flight["from_city"] == city or flight["to_city"] == city
        ]
    elif search_criteria == 2:
        
        city = input("Enter the city: ")
        filtered_flights = [
            flight for flight in flight_table if flight["from_city"] == city
        ]
    elif search_criteria == 3:
        
        from_city = input("Enter the source city: ")
        to_city = input("Enter the destination city: ")
        filtered_flights = [
            flight for flight in flight_table if flight["from_city"] == from_city and flight["to_city"] == to_city
        ]
    else:
        print("Invalid search criteria.")
        return

    print("The following flights match your search criteria:")
    for flight in filtered_flights:
        print(f"Flight ID: {flight['flight_id']}")
        print(f"From: {flight['from_city']}")
        print(f"To: {flight['to_city']}")
        print(f"Price: {flight['price']}")
        print()


def main():
    flight_table = get_flight_table()

    search_criteria = int(input("Enter the search criteria (1, 2, or 3): "))

    search_flights(flight_table, search_criteria)


if __name__ == "__main__":
    main()

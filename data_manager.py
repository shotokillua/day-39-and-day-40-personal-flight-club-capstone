import requests
from pprint import pprint

sheety_endpoint = "https://api.sheety.co/cb445a9d042d09272a19cd2dfcf3482e/flightDealsTmt/prices"
sheety_users_endpoint = "https://api.sheety.co/cb445a9d042d09272a19cd2dfcf3482e/flightDealsTmt/users"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(sheety_endpoint)
        data = response.json()["prices"]
        self.destination_data = data
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_iata_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{sheety_endpoint}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = sheety_users_endpoint
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

